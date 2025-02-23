import mnist
import numpy as np
import matplotlib.pyplot as plt


# Perceptron wilowarstwowy
# składa sie z conajmniej trzech wartstw neuronów

def transform_linear(x: np.ndarray, w: np.ndarray, b: np.ndarray) -> np.ndarray:
    """

    :param x:
    :param w:
    :param b:
    :return:  result of x.dot(w) + b
    """

    return x @ w + b  # @ to samo co dot


dummy_x = np.random.normal(0, 1, size=(10, 128))
dummy_w = np.random.normal(0, 1, size=(128, 256))
dummy_b = np.random.normal(0, 1, size=(256,))

dummy_out = transform_linear(dummy_x, dummy_w, dummy_b)
print(dummy_out.shape)  # (10, 256)


def relu(x: np.ndarray) -> np.ndarray:
    return np.maximum(x, 0)


dummy_x = np.arange(36).reshape(6, 6) - 18
print(dummy_x)

print(relu(dummy_x))


# [[ 0  0  0  0  0  0]
#  [ 0  0  0  0  0  0]
#  [ 0  0  0  0  0  0]
#  [ 0  1  2  3  4  5]
#  [ 6  7  8  9 10 11]
#  [12 13 14 15 16 17]]

def softmax(x: np.ndarray, axis: int = -1) -> np.ndarray:
    x -= np.max(x, axis=axis, keepdims=True)
    e = np.exp(x)
    return e / np.sum(e, axis=axis, keepdims=True)


dummy_x = np.array([
    [3.7, 14.21, 57.89, 27.32],
    [21.33, 9.12, 33.21, 16.81],
    [0.0, 12.31, 19.81, 19.81],
])

softmax_out = softmax(dummy_x)

print(softmax_out)
print(softmax_out.shape)

# plt.plot(np.arange(4), dummy_x[1])
# plt.plot(np.arange(4), softmax_out[1])
# plt.show()

from typing import List, Tuple, Callable

ActivationFunction = Callable[[np.ndarray], np.ndarray]
Layer = Tuple[np.ndarray, np.ndarray, ActivationFunction]

WEIGHT_PATH = "./mlp_weights.npz"


def load_model(weights_path: str) -> List[Layer]:
    weights = np.load(weights_path)
    model_activations = [relu, relu, softmax]
    model = []
    for layer_idx, layer_activation in enumerate(model_activations):
        model.append(
            (
                weights[f"layer_{layer_idx}/W"],
                weights[f"layer_{layer_idx}/b"],
                layer_activation
            )
        )
    return model


model = load_model(weights_path=WEIGHT_PATH)
IMAGE_SIZE = 28 * 28


def infer_from_model(model: List[Layer],
                     x: np.ndarray,
                     flatten_input: bool = False) -> np.ndarray:
    if flatten_input:
        x = x.reshape(-1, IMAGE_SIZE)
    for w, b, activation in model:
        x = transform_linear(x=x, w=w, b=b)
        x = activation(x)
    return np.argmax(x, axis=-1)


dummy_x = np.random.normal(0, 1, size=(5, IMAGE_SIZE))
dummy_inference = infer_from_model(model=model, x=dummy_x)
print(dummy_inference)
# błedny url w bibliotece
# mnist_test_images = mnist.test_images().astype(np.float32) / 255.0
# mnist_test_labels = mnist.test_labels()
# w zamian uzyjemy Tensorflow do pobrania tych danych

from tensorflow.keras.datasets import mnist

(mnist_train_images, mnist_train_labels), (mnist_test_images, mnist_test_labels) = mnist.load_data()
mnist_test_images = mnist_test_images.astype(np.float32) / 255.0
mnist_train_images = mnist_train_images.astype(np.float32) / 255.0

print(mnist_test_images.shape)
print(mnist_test_labels.shape)

def infer_on_rqandom_sample(dataset: np.ndarray, labels: np.ndarray, model: List[Layer]) -> None:
    example_idx = np.random.choice(np.arange(mnist_test_images.shape[0]))
    example = dataset[example_idx]
    gt_label = labels[example_idx]

