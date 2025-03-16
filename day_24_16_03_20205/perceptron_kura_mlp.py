# siec MLP - wielowarstwowy perceptron

import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def sigmoid_derivative(x):
    return x * (1 - x)


# dane
# liczba końćzyn, sierść, pióra, waga, ogon
X = np.array([
    [4, 1, 0, 4, 1],  # kot
    [4, 1, 0, 20, 1],  # pies
    [2, 0, 1, 1.5, 0],  # kura
    [4, 1, 0, 5, 1],  # kot
    [4, 1, 0, 25, 1],  # pies
    [2, 0, 1, 2, 0],  # kura
])

y = np.array([
    [1, 0, 0],  # kot
    [0, 1, 0],  # pies
    [0, 0, 1],  # kura
    [1, 0, 0],  # kot
    [0, 1, 0],  # pies
    [0, 0, 1],  # kura
])

# stabilizacja danych
# w celu szybszej nauki
# min-max
X = X / np.max(X, axis=0)

# ustawienai modelu
input_neurons = X.shape[1]  # 5 neuronów
hidden_neurons = 4  # 4 neurony
output_neurons = y.shape[1]  # 3 wyjscia
learning_rate = 0.5
epochs = 10000

W_input_hidden = np.random.uniform(-1, 1, (input_neurons, hidden_neurons))
W_hidden_output = np.random.uniform(-1, 1, (hidden_neurons, output_neurons))

# trenowanie MLP
for epoch in range(epochs):
    hidden_input = np.dot(X, W_input_hidden)
    hidden_output = sigmoid(hidden_input)

    final_input = np.dot(hidden_output, W_hidden_output)
    final_output = sigmoid(final_input)

    error = y - final_output

    # backpropagation
    d_output = error * sigmoid_derivative(final_output)
    error_hidden = d_output.dot(W_hidden_output.T)
    d_hidden = error_hidden * sigmoid_derivative(hidden_output)

    W_hidden_output += hidden_output.T.dot(d_output) * learning_rate
    W_input_hidden += X.T.dot(d_hidden) * learning_rate

    if epoch % 1000 == 0:
        loss = np.mean(np.abs(error))
        print(f"Epoka {epoch}, Błąd: {loss:.4f}")

print("Trening zakońćzony")

test_data = np.array([
    [4, 1, 0, 6, 1],  # kot
    [4, 1, 0, 30, 1],  # pies
    [2, 0, 1, 1.8, 0],  # kura
    [2, 0, 1, 3.8, 0],  # kura
    [4, 1, 0, 10, 1],  # kot
    [4, 1, 0, 18, 1],  # Zwierzę 6: Pies
])

test_data = test_data / np.max(test_data, axis=0)  # normalizacja danych

# przewidywanie
hidden_input = np.dot(test_data, W_input_hidden)
hidden_output = sigmoid(hidden_input)
final_input = np.dot(hidden_output, W_hidden_output)
final_output = sigmoid(final_input)

print("Przewidywane kalsy:")
for i, pred in enumerate(final_output):
    predicted_class = np.argmax(pred)
    class_names = ["Kot", "Pies", "Kura"]
    print(f"Zwierzę {i + 1}: {class_names[predicted_class]}")

# Epoka 0, Błąd: 0.4887
# Epoka 1000, Błąd: 0.0250
# Epoka 2000, Błąd: 0.0163
# Epoka 3000, Błąd: 0.0129
# Epoka 4000, Błąd: 0.0110
# Trening zakońćzony
# Przewidywane kalsy:
# Zwierzę 1: Kot
# Zwierzę 2: Pies
# Zwierzę 3: Kura
# Zwierzę 4: Kura
# Zwierzę 5: Kot
# Zwierzę 6: Pies
