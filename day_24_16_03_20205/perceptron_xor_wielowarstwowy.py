# perceptron wielowarstwowy
import numpy as np


# warstwa wejsciowa
# warstwa ukryta
# warstwa wyjscia (klasyfikcja)

# funkcja aktywacji sigmoid
def sigmoid(x):
    return 1 / (1 + np.exp(-x))


# dane wejsciowe
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([0, 1, 1, 0])  # oczekiwany wynik

# warstwa ukryta 2 neurony
# ręcznie ustawione wagi i bias
W1 = np.array([[1, 1], [1, 1]])
# b1 = np.array([-1, 0])
b1 = np.array([-1.5, 0.5])

# warstwa wyjsciowa 1 neuron
# W2 = np.array([1, -2])
W2 = np.array([1, -1])
# b2 = -1
b2 = -0.5

for x in X:
    print(x)

    # warstwa ukryta
    hidden_input = np.dot(x, W1) + b1
    hidden_output = sigmoid(hidden_input)

    # warstwa wyjsciowa
    output_input = np.dot(hidden_output, W2) + b2
    output = sigmoid(output_input)

    print(f"Wejscie: {x}, Wyjście: {output}")
    print(f"Wejscie: {x}, Wyjście: {int(output > 0.5)}")
