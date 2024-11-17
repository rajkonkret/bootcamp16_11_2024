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
