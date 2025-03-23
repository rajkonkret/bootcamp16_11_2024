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
print(x_data.shape)
