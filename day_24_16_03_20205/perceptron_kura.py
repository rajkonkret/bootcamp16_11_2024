import numpy as np


def activation_function(x):
    return np.where(x >= 0, 1, 0)


class Perceptron:
    def __init__(self, input_size, learnig_rate=0.1, epochs=100):
        self.learning_rate = learnig_rate
        self.epochs = epochs
        self.weights = np.random.randn(input_size, 3)  # (kot, pies, kura)
        self.bias = np.random.randn(3)

    def fit(self, X, y):
        for _ in range(self.epochs):
            for i in range(len(X)):
                linear_output = np.dot(X[i], self.weights) + self.bias
                y_pred = activation_function(linear_output)

                error = y[i] - y_pred
                self.weights += self.learning_rate * np.outer(X[i], error)
                self.bias += self.learning_rate * error

    def predict(self, X):
        linear_output = np.dot(X, self.weights) + self.bias
        y_pred = activation_function(linear_output)
        return np.argmax(y_pred, axis=1)  # indeks klasy


# dane wejsciowe ilość kończyn, sierść, pióra, wielkość, waga
X = np.array([
    [4, 1, 0, 0.3, 4],  # kot
    [4, 1, 0, 0.5, 10],  # pies
    [2, 0, 1, 0.2, 3],  # kura
    [4, 1, 0, 0.35, 5],  # kot (trochę większy)
    [4, 1, 0, 0.55, 12],  # większy pies
    [2, 0, 1, 0.25, 2.5],  # mniejsza kura
])

y = np.array([
    [1, 0, 0],  # "kot"
    [0, 1, 0],  # "pies"
    [0, 0, 1],  # "kura"
    [1, 0, 0],  # "kot"
    [0, 1, 0],  # "pies"
    [0, 0, 1],  # "kura"
])

# trening perceptronu
perceptron = Perceptron(input_size=5)
perceptron.fit(X, y)

test_data = np.array([
    [4, 1, 0, 0.4, 6],  # kot
    [4, 1, 0, 0.6, 15],  # pies
    [2, 0, 1, 0.22, 3],  # kura
])

predictions = perceptron.predict(test_data)

animals = ["Kot", "Pies", 'Kura']
for i, prediction in enumerate(predictions):
    print(f"Dane wejściowe: {test_data[i]}, Rozpoznano: {animals[prediction]}")

# Dane wejściowe: [4.  1.  0.  0.4 6. ], Rozpoznano: Kot
# Dane wejściowe: [ 4.   1.   0.   0.6 15. ], Rozpoznano: Pies
# Dane wejściowe: [2.   0.   1.   0.22 3.  ], Rozpoznano: Kura
