import numpy as np
# ReLU

def relu(x):
    return np.maximum(0, x)


def relu_derivative(x):
    return np.where(x > 0, 1, 0)


# XOR
# dane treningowe
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [1], [1], [0]])

np.random.seed(42)
W_hidden = np.random.rand(2, 2) * 2 - 1
W_output = np.random.rand(2, 1) * 2 - 1

learning_rate = 0.01
epochs = 50000

# trening sieci
for epoch in range(epochs):
    hidden_input = np.dot(X, W_hidden)
    hidden_output = relu(hidden_input)  # ReLU

    final_input = np.dot(hidden_output, W_output)
    final_output = relu(final_input)

    # obliczenie błedu
    error = y - final_output

    # backpropagation
    d_output = error * relu_derivative(final_output)  # pochodna relu
    error_hidden = d_output.dot(W_output.T)
    d_hidden = error_hidden * relu_derivative(hidden_output)

    W_output += hidden_output.T.dot(d_output) * learning_rate
    W_hidden += X.T.dot(d_hidden) * learning_rate

# Tesowanie
# Testowanie XOR
for i in range(4):
    hidden_layer_input = np.dot(X[i], W_hidden)
    hidden_layer_output = relu(hidden_layer_input)

    final_input = np.dot(hidden_layer_output, W_output)
    final_output = relu(final_input)

    print(f"Wejscie: {X[i]} -> Przewidywane wyjście: {final_output[0]:.4f}")

# Wejscie: [0 0] -> Przewidywane wyjście: 0.0000
# Wejscie: [0 1] -> Przewidywane wyjście: 0.0000
# Wejscie: [1 0] -> Przewidywane wyjście: 0.0000
# Wejscie: [1 1] -> Przewidywane wyjście: 0.0000
