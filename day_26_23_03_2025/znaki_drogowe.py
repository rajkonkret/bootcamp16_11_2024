# benchmark.ini.rub.de
# https://sid.erda.dk/public/archives/daaeac0d7ce1152aea9b61d9f1e19370/published-archive.html
# https://drive.proton.me/urls/NESBAMQ2XW#6WqlPYbAtmu5

# pip install opencv-python opencv-contrib-python

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


def load_gtrsb_data(data_dir, img_size=(32, 32)):
    images = []
    labels = []
    for class_id in range(43):
        class_path = os.path.join(data_dir, f"{class_id:05d}")
        print(class_path)
        if os.path.exists(class_path):
            for img_name in os.listdir(class_path):
                img_path = os.path.join(class_path, img_name)
                img = cv2.imread(img_path)
                # cv2.imshow("Podgląd obrazu", img)
                # cv2.waitKey(0)
                # cv2.destroyAllWindows()
                if img is not None:
                    img = cv2.resize(img, img_size)
                    images.append(img)
                    labels.append(class_id)
                else:
                    print(f"Warnning: Could not load image: {img_path}")
    return np.array(images), np.array(labels)


train_dir = r"gtrsb/files/GTSRB/Training/Images"

x_data, y_data = load_gtrsb_data(train_dir)
np.savez("gtrsb_dataset.npz", x=x_data, y=y_data)
print(x_data.shape)  # (39209, 32, 32, 3)

# normalizacja obrazow
x_data = x_data.astype("float32") / 255.0

# one hot encoding
y_data = to_categorical(y_data, num_classes=43)

x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size=0.2, random_state=42)

model = keras.Sequential([
    layers.Flatten(input_shape=(32, 32, 3)),
    layers.Dense(512, activation='relu'),
    layers.Dense(256, activation='relu'),
    layers.Dense(43, activation="softmax")
])

model.compile(optimizer="adam",
              loss='categorical_crossentropy',
              metrics=['accuracy'])

history = model.fit(
    x_train,
    y_train,
    epochs=10,
    validation_data=(x_test, y_test),
    batch_size=32
)

model.save('gtrsb_model.keras')
print("Model został zapisany")

# wizualizacja dokładności
plt.plot(history.history['accuracy'], label='Train Accuracy')
plt.plot(history.history['val_accuracy'], label='Test Accuracy')
plt.xlabel("Epoka")
plt.ylabel("dokładność")
plt.legend()
plt.show()
