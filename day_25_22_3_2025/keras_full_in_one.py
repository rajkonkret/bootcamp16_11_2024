import os
import numpy as np
import time

os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"  # wyłaczenie optymalizacji dla Tensorflow
import tensorflow as tf
from tensorflow import keras
from keras import Input
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

print("Dostępne urządzenia:", tf.config.list_physical_devices())

X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

y = np.array([
    [0, 0, 0],  # and, or, xor
    [0, 1, 1],  # and, or, xor
    [0, 1, 1],  # and, or, xor
    [1, 1, 0],  # and, or, xor
])

# tworzymy model
# 2 wejscia
# 4 neurony warstwa ukryta
# 3 neurony warstwa wyjscia
model = Sequential([
    Input(shape=(2,)),
    Dense(4, activation="relu"),  # warstwa ukryta
    Dense(3, activation="sigmoid")  # warstwa wyjściowa
])

# kompilacja modelu
model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])

start_time = time.time()

with tf.device("/GPU:0"):
    model.fit(X, y, epochs=2000, verbose=1)

print(f"Estimated time: {time.time() - start_time}")

# testownie modelu
predictions = model.predict(X)
predictions = (predictions > 0.5).astype(int)

print("Przewidywane wartości dla AND, OR, XOR\n")
for i in range(len(X)):
    print(f"Wejscie {X[i]} => AND: {predictions[i][0]}, OR {predictions[i][1]}, XOR: {predictions[i][2]}")

# zapisanie modelu
model.save("logic_gates.keras")

# zapisanie wag i biasów z modelu numpy
weights = model.get_weights()

filename = "weights_only.npz"
np.savez(filename, *weights)
print("Wagi zapisane do pliku", filename)
