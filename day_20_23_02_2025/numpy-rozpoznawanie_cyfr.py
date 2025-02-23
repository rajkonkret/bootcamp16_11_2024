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

plt.plot(np.arange(4), dummy_x[1])
plt.plot(np.arange(4), softmax_out[1])
plt.show()

from typing import List, Tuple, Callable

ActivationFunction = Callable[[np.ndarray], np.ndarray]
Layer = Tuple[np.ndarray, np.ndarray, ActivationFunction]

