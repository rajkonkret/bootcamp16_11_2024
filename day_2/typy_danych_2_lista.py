# kolekcje
# lista - kolekcja przechowująca dowolną ilość danych dowolnego typu w jenej kolekcji
# mogą byż listy przechowujące mieszane dane (str i int etc...)
# lista zachowuje kolejność przy dodawaniu elementów

lista = []
print(lista)  # []
print(type(lista))  # <class 'list'>
print(bool(lista))  # False dla pustej listy

pusta_lista = list()
print(type(pusta_lista))  # <class 'list'>
print(pusta_lista)  # []

# deklaracja listy i wypełnienie jej danymi w miejscu deklaracji
lista_2 = [10, 20, 30]
print(type(lista_2))  # <class 'list'>
print(lista_2)  # [10, 20, 30]

lista_3 = [10.77, 30.66, 67, 15]
print(type(lista_3))  # <class 'list'>
print(lista_3)  # [10.77, 30.66, 67, 15]

# lista mmieszana
lista_mieszana = [10, 5.2, "Oko", "Radek"]
print(type(lista_mieszana))  # <class 'list'>
print(lista_mieszana)  # [10, 5.2, 'Oko', 'Radek']

# sprawdzenie ile elemntów znajduje się w kolekcji
print(len(lista_mieszana))  # długosć 4 elementy

# [10, 5.2, 'Oko', 'Radek']
#   0   1     2       3

# dodawanie elementu do listy, na końcu
lista.append("Radek")
lista.append("Maciek")
lista.append("Tomek")
lista.append("Zenek")
lista.append("Marta")
lista.append("Anna")
print(lista)  # ['Radek', 'Maciek', 'Tomek', 'Zenek', 'Marta', 'Anna']
print(type(lista))  # <class 'list'>
print(len(lista))  # długość 6 elementów

# ['Radek', 'Maciek', 'Tomek', 'Zenek', 'Marta', 'Anna']
#     0       1          2        3        4        5
#     -6      -5         -4       -3       -2       -1
print(lista[1])  # Maciek
print(lista[5])  # Anna
print(lista[3])  # Zenek

print(lista[len(lista) - 1])  # ostatni element z listy, Anna
print(lista[-1], lista[5])  # Anna Anna
print(lista[-2], lista[4])  # Marta Marta
print(lista[-3], lista[3])  # Zenek Zenek
print(lista[-4], lista[2])  # Tomek Tomek
print(lista[-5], lista[1])  # Maciek Maciek
print(lista[-6], lista[0])  # Radek Radek

# print(lista[10]) - lista nie posiada elementu o takim indeksie
# Traceback (most  recent call last):
#   File "C:\Users\Administrator\PycharmProjects\bootcamp16_11_2024\day_2\typy_danych_2_lista.py", line 61, in <module>
#     print(lista[10])
#           ~~~~~^^^^
# IndexError: list index out of range
#
# Process finished with exit code 1

# wypisywanie wielu elementów z listy (slicowanie)
# ['Radek', 'Maciek', 'Tomek', 'Zenek', 'Marta', 'Anna']
#    -6        -5        -4       -3       -2       -1
#     0         1         2        3        4        5
print(lista[0:3])  # ['Radek', 'Maciek', 'Tomek']
print(lista[1:3])  # ['Maciek', 'Tomek']
print(lista[:3])  # ['Radek', 'Maciek', 'Tomek']
print(lista[:2])  # ['Radek', 'Maciek']
print(lista[-3:])  # ['Zenek', 'Marta', 'Anna']
print(lista[-2:])  # ['Marta', 'Anna']
print(lista[-1:])  # ['Anna']
print(lista[-1])  # Anna
print(lista[-1:][0])  # Anna
print(lista[-1][0])  # A
print(lista[:])  # ['Radek', 'Maciek', 'Tomek', 'Zenek', 'Marta', 'Anna'] ->012345
print(lista[2:5])  # ['Tomek', 'Zenek', 'Marta']
print(lista[2:])  # ['Tomek', 'Zenek', 'Marta', 'Anna']

print(lista[-3:0])  # [] -> [3:0]
print(lista[0:-3])  # [0:3] -> ['Radek', 'Maciek', 'Tomek']

print(lista[2:2])  # []
print(lista[4:10])  # ['Marta', 'Anna']
print(lista[7:11])  # []

# nadpisanie elementu w liscie na wskazanym indeksie
lista[2] = "Mikołaj"
print(lista)  # ['Radek', 'Maciek', 'Mikołaj', 'Zenek', 'Marta', 'Anna']
print(len(lista))  # długość 6

# rozszerzenie listy, wstawienie elementu na wskazanym indeksie
lista.insert(1, "Karolina")
print(lista)  # ['Radek', 'Karolina', 'Maciek', 'Mikołaj', 'Zenek', 'Marta', 'Anna']
print(len(lista))  # długość 7

# usunięcie elemntu z listy
# 1. usunięcie po indeksie -> pop()
# 2. usunięcie po elemencie -> remove()

# po indeksie pop() - zwraca informację co usunął
print(lista.pop(0))  # Radek
print(lista)  # ['Karolina', 'Maciek', 'Mikołaj', 'Zenek', 'Marta', 'Anna']
ind = lista.index("Zenek")  # pierwszy napotkany
print("Numer indeksu dla Zenek:", ind)
print(lista.pop(ind))  # Zenek
print(lista)  # ['Karolina', 'Maciek', 'Mikołaj', 'Marta', 'Anna']
print(lista.pop())  # w liście to usunie ostatni element, Anna

# usunięcie po elemencie, pierwszy napotkany
lista.append("Maciek")
print(lista)  # ['Karolina', 'Maciek', 'Mikołaj', 'Marta', 'Maciek']
lista.remove("Maciek")
print(lista)  # ['Karolina', 'Mikołaj', 'Marta', 'Maciek']

# print(lista.remove("Zenek")) # ValueError: list.remove(x): x not in list, nie ma takiego elementu
print("Marta" in lista)  # True
print("Zenek" in lista)  # False

print(lista.remove("Marta"))  # None
print(lista)  # ['Karolina', 'Mikołaj', 'Maciek']

lista.append("Marta")
lista.append("Marta")
lista.append("Marcin")
print(lista)  # ['Karolina', 'Mikołaj', 'Maciek', 'Marta', 'Marta', 'Marcin']
print(lista.index("Marta"))  # indeks: 3

a = 1
b = 3
a = b
print(f"{a=}")
print(f"{b=}")
# a=3
# b=3
b = 7
print(f"{a=}")  # a=3
print(f"{b=}")  # b=7

lista_4 = lista  # a = b, kopiowanie referencji, adres w pamięci
print(f"{lista=}")
print(f"{lista_4=}")
lista_copy = lista.copy()  # kopia elemntów listy do innej listy
# lista = ['Karolina', 'Mikołaj', 'Maciek', 'Marta', 'Marta', 'Marcin']
# lista_4 = ['Karolina', 'Mikołaj', 'Maciek', 'Marta', 'Marta', 'Marcin']
lista.clear()  # usunięcie elementów z listy
print(f"{lista=}")
print(f"{lista_4=}")
print(f"{lista_copy=}")
# lista=[]
# lista_4=[]
# lista_copy=['Karolina', 'Mikołaj', 'Maciek', 'Marta', 'Marta', 'Marcin']
# obie listy zostały zmienione
# wskazują na ten sam adres w pamięci
# id() - podaje adres dla danej listy
print(f"adres: {id(lista)=}")
print(f"adres: {id(lista_4)=}")
print(f"adres: {id(lista_copy)=}")
# adres: id(lista)=1746325475712
# adres: id(lista_4)=1746325475712
# adres: id(lista_copy)=1746328345216
