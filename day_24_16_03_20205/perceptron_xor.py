import numpy as np


def xor(a, b):
    return int(a != b)


print(xor(0, 0))  # 0
print(xor(0, 1))  # 1
print(xor(1, 0))  # 1
print(xor(1, 1))  # 0


class Perceptron:
    def __init__(self, learning_rate=0.1, epochs=10):
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.weights = None
        self.bias = None

    def activation_function(self, x):
        return 1 if x >= 0 else 0

    def fit(self, X, y):
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0

        for _ in range(self.epochs):
            for i in range(n_samples):
                linear_output = np.dot(X[i], self.weights) + self.bias
                y_predicted = self.activation_function(linear_output)

                update = self.learning_rate * (y[i] - y_predicted)
                self.weights += update * X[i]
                self.bias += update

    def predict(self, X):
        print(self.weights)
        print(self.bias)
        linear_output = np.dot(X, self.weights) + self.bias
        return np.array([self.activation_function(x) for x in linear_output])


# dane treningowe dla XOR
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])  # dane testowe
y = np.array([0, 1, 1, 0])  # prawidłowe odpowiedzi
print(X.dtype)  # int64

# trening perceptronu
p = Perceptron(learning_rate=0.1, epochs=10)
p.fit(X, y)

# testowanie perceptronu
predictions = p.predict(X)
print("Przewidywane wyniki", predictions)  # bład Przewidywane wyniki [1 1 0 0]
# int64
# [-0.1  0. ]
# 0.0
# Przewidywane wyniki [1 1 0 0] # błędne dane

# dane treningowe dla XOR
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])  # dane testowe
y = np.array([0, 1, 1, 0])  # prawidłowe odpowiedzi
print(X.dtype)  # int64

# trening perceptronu
p = Perceptron(learning_rate=0.01, epochs=500)
p.fit(X, y)

# testowanie perceptronu
predictions = p.predict(X)
print("Przewidywane wyniki", predictions)  # nadal jest żle Przewidywane wyniki [1 1 0 0]

# dane treningowe dla XOR
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])  # dane testowe
y = np.array([0, 1, 1, 0])  # prawidłowe odpowiedzi
print(X.dtype)  # int64

# trening perceptronu
p = Perceptron(learning_rate=0.1, epochs=100)
p.fit(X, y)

# testowanie perceptronu
predictions = p.predict(X)
print("Przewidywane wyniki", predictions)  # nadal żle Przewidywane wyniki [1 1 0 0]
