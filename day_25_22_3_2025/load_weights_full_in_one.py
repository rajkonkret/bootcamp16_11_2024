import numpy as np

# wczytanie modelu
loaded_weights = np.load("weights_only_ok.npz")

print("Dostępne parametry:")
print(loaded_weights.files)  # ['arr_0', 'arr_1', 'arr_2', 'arr_3']

param_name = loaded_weights.files[0]
param_array = loaded_weights[param_name]

print(f"Parametr: {param_name}")  # Parametr: arr_0
print(f"Kształt: {param_array.shape}")  # Kształt: (2, 4)
print(f"Dane: {param_array.flatten()[:5]}")  # Dane: [ 2.1389737   1.7770367  -0.35845113 -1.6961273  -1.6722467 ]

W_input_hidden = loaded_weights["arr_0"]  # wagi ukryta - wejscie
b_hidden = loaded_weights["arr_1"]  # bias warstwy ukrytej
W_hidden_output = loaded_weights['arr_2']  # wyjscie warstwy ukrytej
b_output = loaded_weights['arr_3']  # bias wyjscia

X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1],
])


def relu(x):
    return np.maximum(0, x)


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


# warstwa ukryta
hidden_layer = np.dot(X, W_input_hidden) + b_hidden
hidden_layer = relu(hidden_layer)

# warstwa wyjściowa
predictions = np.dot(hidden_layer, W_hidden_output) + b_output
predictions = sigmoid(predictions)

print("Predictions shape:", predictions.shape)  # Predictions shape: (4, 3)

# konwersja 0/1
predictions = (predictions > 0.5).astype(int)

y_expected = np.array([
    [0, 0, 0],  # and, or, xor
    [0, 1, 1],
    [0, 1, 1],
    [1, 1, 0],
])

print("Przewidywanie wartości dla AND, OR, XOR:\n")
for i in range(len(X)):
    print(f"Wejście: {X[i]} => AND: {predictions[i][0]}, OR {predictions[i][1]}, XOR {predictions[i][2]}")
