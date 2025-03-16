import numpy as np
import matplotlib.pyplot as plt


# perceptron - matematyczne odzwierciedlenie neuronu
# przyjmuje zestaw danych
# na podstawie danych wejsciowych ustala wagi i dodakowe przesunięcie taka by jak najbardziej przewidziany wynik był własciwy
# suma ważona z = x*w + b

# funkcja aktywacji - funkcja ktora daaje wynik działąnia perceptronu
# np funkcja skokowa wartości 0 lub 1
# perceptron binarny 

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

    def set_fit(self):
        self.weights = np.array([0.2, 0.1])
        self.bias = -0.20000000000000004

    def predict(self, X):
        print(self.weights)
        print(self.bias)
        linear_output = np.dot(X, self.weights) + self.bias
        return np.array([self.activation_function(x) for x in linear_output])


def plot_decision_boundary(X, y, model):
    x_min, x_max = -0.5, 1.5
    y_min, y_max = -0.5, 1.5
    xx, yy = np.meshgrid(np.linspace(x_min, x_max, 100),
                         np.linspace(y_min, y_max, 100))

    Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)

    plt.contourf(xx, yy, Z, alpha=0.3, cmap=plt.cm.Paired)
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Paired, edgecolors="k")
    plt.title("Podział obszaru decyzyjnego")
    plt.xlabel("X1")
    plt.ylabel("X2")
    plt.show()


# AND
# 0 and 0 = 0
# 0 and 1 = 0
# 1 and 0 = 0
# 1 and 1 = 1

# dane treningowe
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])  # dane testowe
y = np.array([0, 0, 0, 1])  # prawidłowe odpowiedzi
print(X.dtype)  # int64

# trening perceptronu
p = Perceptron(learning_rate=0.1, epochs=10)
p.fit(X, y)

# testowanie perceptronu
predictions = p.predict(X)
print("Przewidywane wyniki", predictions)  # Przewidywane wyniki [0 0 0 1]

p = Perceptron(learning_rate=0.1, epochs=5)
p.fit(X, y)

# testowanie perceptronu
predictions = p.predict(X)
print("Przewidywane wyniki", predictions)  # Przewidywane wyniki [0 0 0 1]

p = Perceptron(learning_rate=0.1, epochs=2)
p.fit(X, y)

# testowanie perceptronu
predictions = p.predict(X)
print("Przewidywane wyniki", predictions)  # Przewidywane wyniki [0 1 1 1]

p = Perceptron(learning_rate=0.01, epochs=5)
p.fit(X, y)

# testowanie perceptronu
predictions = p.predict(X)
print("Przewidywane wyniki", predictions)  # Przewidywane wyniki [0 0 0 1]

p = Perceptron(learning_rate=0.01, epochs=2)
p.fit(X, y)

# testowanie perceptronu
predictions = p.predict(X)
print("Przewidywane wyniki", predictions)  # Przewidywane wyniki [0 1 1 1]
plot_decision_boundary(X, y, p)
p.set_fit()
# testowanie perceptronu
predictions = p.predict(X)
print("Przewidywane wyniki", predictions)  # Przewidywane wyniki [0 0 0 1]

plot_decision_boundary(X, y, p)

# or
print("Trening OR")
# dane treningowe
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])  # dane testowe
y = np.array([0, 1, 1, 1])  # prawidłowe odpowiedzi
print(X.dtype)  # int64

# trening perceptronu
p = Perceptron(learning_rate=0.1, epochs=10)
p.fit(X, y)
predictions = p.predict(X)
print("Przewidywane wyniki", predictions)  # Przewidywane wyniki [0 1 1 1]
p.set_fit()  # ustawienia dla przewidywania and
predictions = p.predict(X)
print("Przewidywane wyniki", predictions)  # Przewidywane wyniki [0 0 0 1] bład dla OR bo wzięliśmy wagi dla AND
