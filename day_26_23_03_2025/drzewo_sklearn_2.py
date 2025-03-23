import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn import metrics
import matplotlib.pyplot as plt
import numpy as np

dane = [
    {"wiek": 55, "zarobki": 70, "decyzja": "tak"},
    {"wiek": 53, "zarobki": 50, "decyzja": "nie"},
    {"wiek": 47, "zarobki": 60, "decyzja": "tak"},
    {"wiek": 40, "zarobki": 30, "decyzja": "nie"},
    {"wiek": 35, "zarobki": 45, "decyzja": "tak"},
    {"wiek": 28, "zarobki": 65, "decyzja": "nie"},
    {"wiek": 31, "zarobki": 42, "decyzja": "tak"},
    {"wiek": 29, "zarobki": 50, "decyzja": "nie"},
    {"wiek": 52, "zarobki": 80, "decyzja": "tak"},
    {"wiek": 60, "zarobki": 55, "decyzja": "tak"},
]

df = pd.DataFrame(dane)
df['decyzja_bin'] = df["decyzja"].map({"nie": 0, "tak": 1})

X = df[["wiek", "zarobki"]]
y = df["decyzja_bin"]

model = DecisionTreeClassifier(criterion="entropy", max_depth=3, random_state=0)
model.fit(X, y)

# y_pred = model.predict(X)
test_input = pd.DataFrame([
    {"wiek": 34, "zarobki": 60},
    {"wiek": 50, "zarobki": 40},
    {"wiek": 28, "zarobki": 30},
    {"wiek": 45, "zarobki": 65},
    {"wiek": 37, "zarobki": 35},
    {"wiek": 60, "zarobki": 20}
])

predicted = model.predict(test_input)
test_input['predykcja'] = ["tak" if p == 1 else "nie" for p in predicted]
# accuracy = metrics.accuracy_score(y, y_pred)
print("Predykcja dla nowych danych")
print(test_input)

# accuracy = metrics.accuracy_score(y, predicted)
# print(f'Accuracy: {accuracy:.2f}')

plt.figure(figsize=(10, 6))
plot_tree(model, feature_names=["wiek", "zarobki"],
          class_names=["nie", "tak"], filled=True)
plt.title('Drzewo decyzyjne')
plt.show()
# Predykcja dla nowych danych
#    wiek  zarobki predykcja
# 0    34       60       tak
# 1    50       40       nie
# 2    28       30       nie
# 3    45       65       tak
# 4    37       35       tak
# 5    60       20       nie
