import os

os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"

import numpy as np
from tensorflow import keras
from tensorflow.keras import layers
import matplotlib.pyplot as plt
import cv2
from sklearn.model_selection import train_test_split
# pip install scikit-learn
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import load_model

model = load_model("gtrsb_model.keras")
print("Model został załadowany")
model.summary()

data = np.load("gtrsb_dataset.npz")
x_data = data["x"]
y_data = data["y"]
print(x_data.shape)

# normalizacja obrazow
x_data = x_data.astype("float32") / 255.0

# one hot encoding
y_data = to_categorical(y_data, num_classes=43)

x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size=0.2, random_state=42)

# ewaluacja modelu
test_loss, test_acc = model.evaluate(x_test, y_test, verbose=2)
print(f"Finalna dokładność testowa: {test_acc:.2f}")

labels_map = {
    0: "Ograniczenie prędkości (20 km/h)",
    1: "Ograniczenie prędkości (30 km/h)",
    2: "Ograniczenie prędkości (50 km/h)",
    3: "Ograniczenie prędkości (60 km/h)",
    4: "Ograniczenie prędkości (70 km/h)",
    5: "Ograniczenie prędkości (80 km/h)",
    6: "Koniec ograniczenia prędkości (80 km/h)",
    7: "Ograniczenie prędkości (100 km/h)",
    8: "Ograniczenie prędkości (120 km/h)",
    9: "Zakaz wyprzedzania",
    10: "Zakaz wyprzedzania dla pojazdów > 3.5 ton",
    11: "Pierwszeństwo na skrzyżowaniu",
    12: "Droga z pierwszeństwem",
    13: "Ustąp pierwszeństwa",
    14: "STOP",
    15: "Zakaz ruchu",
    16: "Zakaz ruchu pojazdów > 3.5 ton",
    17: "Zakaz wjazdu",
    18: "Ostrzeżenie o niebezpieczeństwie",
    19: "Niebezpieczny zakręt w lewo",
    20: "Niebezpieczny zakręt w prawo",
    21: "Podwójny zakręt",
    22: "Nierówna droga",
    23: "Śliska nawierzchnia",
    24: "Zwężenie drogi po prawej",
    25: "Roboty drogowe",
    26: "Sygnalizacja świetlna",
    27: "Przejście dla pieszych",
    28: "Przejście dla dzieci",
    29: "Przejście dla rowerzystów",
    30: "Uwaga na lód / śnieg",
    31: "Uwaga na dzikie zwierzęta",
    32: "Koniec ograniczenia prędkości i zakazu wyprzedzania",
    33: "Nakaz skrętu w prawo",
    34: "Nakaz skrętu w lewo",
    35: "Nakaz jazdy prosto",
    36: "Nakaz jazdy prosto lub w prawo",
    37: "Nakaz jazdy prosto lub w lewo",
    38: "Nakaz jazdy po prawej stronie jezdni",
    39: "Nakaz jazdy po lewej stronie jezdni",
    40: "Nakaz jazdy okrężnej (rondo)",
    41: "Koniec zakazu wyprzedzania",
    42: "Koniec zakazu wyprzedzania dla pojazdów > 3.5 ton"
}

