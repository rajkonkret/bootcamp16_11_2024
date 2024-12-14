# pickle - serializacja i deserializacja obiektów
import pickle

lista = [1, 2, 3, 4, 5]
# zapisac liste do pliku
# odczytac liste z pliku
# sprawdzic typ

with open("lista.txt", "w") as f:
    f.write(str(lista))

with open("lista.txt", "r") as file:
    lines = file.read()

print(lines)  # [1, 2, 3, 4, 5]
print(type(lines))  # <class 'str'>
print(lines[0])  # [
l = []
l.extend(lines)
print(l)  # ['[', '1', ',', ' ', '2', ',', ' ', '3', ',', ' ', '4', ',', ' ', '5', ']']

with open("lista.pickle", 'wb') as f:
    pickle.dump(lista, f)  # zapis listy do pliku w postaci bajtowej

with open("lista.pickle", 'rb') as fh:
    p = pickle.load(fh)

print(p)  # [1, 2, 3, 4, 5]
print(type(p))  # <class 'list'>
print(p[0])  # 1

# zamiana listy na bajty
lister_ser = pickle.dumps(lista)
print(lister_ser)  # b'\x80\x04\x95\x0f\x00\x00\x00\x00\x00\x00\x00]\x94(K\x01K\x02K\x03K\x04K\x05e.'
# zamian bajtów na listę
wynik = pickle.loads(lister_ser)
print(pickle.loads(lister_ser))  # [1, 2, 3, 4, 5]
print("Wynik deserializacji:", wynik)  # Wynik deserializacji: [1, 2, 3, 4, 5]
print(type(wynik))  # <class 'list'>
