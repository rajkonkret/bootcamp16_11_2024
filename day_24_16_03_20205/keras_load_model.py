import os

import numpy as np

os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"  # przed importowaniem kerasa
from tensorflow.keras.models import load_model

model = load_model("model_and.keras")
# kompilacja modelu
model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])
model.summary()
input()
# Model: "sequential_2"
# ┌─────────────────────────────────┬────────────────────────┬───────────────┐
# │ Layer (type)                    │ Output Shape           │       Param # │
# ├─────────────────────────────────┼────────────────────────┼───────────────┤
# │ dense_4 (Dense)                 │ (None, 4)              │            12 │
# ├─────────────────────────────────┼────────────────────────┼───────────────┤
# │ dense_5 (Dense)                 │ (None, 1)              │             5 │
# └─────────────────────────────────┴────────────────────────┴───────────────┘

# dane wejściowe
X = np.array(
    [[0, 0],
     [0, 1],
     [1, 0],
     [1, 1]]
)


# testowanie mmodelu
predictions = model.predict(X)
predictions = (predictions > 0.5).astype(int)

for i in range(len(X)):
    print(f"{X[i]} {predictions[i]} )")
