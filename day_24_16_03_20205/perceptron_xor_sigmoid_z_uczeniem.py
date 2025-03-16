import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# XOR
# dane treningowe
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [1], [1], [0]])

# AND
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])  # dane testowe
y = np.array([[0], [0], [0], [1]])

np.random.seed(42)
W_hidden = np.random.rand(2, 2)
W_output = np.random.rand(2, 1)

learning_rate = 0.5
epochs = 5000

for epoch in range(epochs):
    # warstawa ukryta
    hidden_input = np.dot(X, W_hidden)
    hidden_output = sigmoid(hidden_input)

    final_input = np.dot(hidden_output, W_output)
    final_output = sigmoid(final_input)

    # błąd
    error = y - final_output

    # aktualizacja wag, backpropagation
    d_output = error * (final_output * (1 - final_output))
    error_hidden = d_output.dot(W_output.T)
    d_hidden = error_hidden * (hidden_output * (1 - hidden_output))

    # aktualizacja wag
    W_output += hidden_output.T.dot(d_output) * learning_rate
    W_hidden += X.T.dot(d_hidden) * learning_rate

# Testowanie XOR
for i in range(4):
    hidden_layer_input = np.dot(X[i], W_hidden)
    hidden_layer_output = sigmoid(hidden_layer_input)

    final_input = np.dot(hidden_layer_output, W_output)
    final_output = sigmoid(final_input)

    print(f"Wejscie: {X[i]} -> Przewidywane wyjście: {final_output[0]:.4f}")
# Wejscie: [0 0] -> Przewidywane wyjście: 0.0943
# Wejscie: [0 1] -> Przewidywane wyjście: 0.8466
# Wejscie: [1 0] -> Przewidywane wyjście: 0.8466
# Wejscie: [1 1] -> Przewidywane wyjście: 0.2026

# dla and
# Wejscie: [0 0] -> Przewidywane wyjście: 0.0026
# Wejscie: [0 1] -> Przewidywane wyjście: 0.0214
# Wejscie: [1 0] -> Przewidywane wyjście: 0.0244
# Wejscie: [1 1] -> Przewidywane wyjście: 0.4976