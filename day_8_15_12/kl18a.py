# stworzyc słownik
# zapisać słownik do pliku za pomocą pickle
# odczytamy słownik
import pickle

slownik = {"name": "Radek", "age": 78}
print(type(slownik))  # <class 'dict'>
print(slownik)  # {'name': 'Radek', 'age': 78}

# pickle używa zapisu bajtowego
# ../ - zapis w katalogu nadrzędnym
with open("../dict1.pkl", "wb") as f:
    pickle.dump(slownik, f)

with open("../dict1.pkl", "rb") as file:
    data = pickle.load(file)

print(data)  # {'name': 'Radek', 'age': 78}
print(type(data))  # <class 'dict'>
print(data['name'])  # Radek
