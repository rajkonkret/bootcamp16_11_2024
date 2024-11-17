# Zbiór (set) - przechowuje unikalne wartości (brak duplikatów)
# nie posiada indeksu
# nie zachowuje kolejności przy dodawaniu elementów

lista = [44, 55, 66, 777, 33, 22, 11, 33, 11]
zbior = set(lista)
print(zbior)  # {33, 66, 777, 11, 44, 22, 55} zmienił kolejność

lista2 = list(zbior)
lista2.remove(33)
print(lista2)  # [66, 777, 11, 44, 22, 55]

# utworzenie pustego seta, zbioru
# Pusty set tylko i wyłącznie za pomocą słówka set()
zb2 = set()
print(zb2)  # pusty zbiór wypisze set()
print(type(zb2))  # <class 'set'>

# dodanie elementów do zbioru
zb2.add(2)
zb2.add(3)
zb2.add(5)
zb2.add(5)
zb2.add(3)  # {2, 3, 5}
print(zb2)

print(zbior)  # {33, 66, 777, 11, 44, 22, 55}
zbior.add(33)
zbior.add(18)
zbior.add(18)
print(zbior)  # {33, 66, 777, 11, 44, 18, 22, 55}

# pop() - usunięcie pierwszego elementu ze zbioru
print(zbior.pop())  # 33, usunął pierwszy elemnt
print(zbior)  # {66, 777, 11, 44, 18, 22, 55}, nie zmienił kolejności

print(zbior.pop())  # 66, kolejny elemnt usunięty

zbior.pop()
zbior.pop()
print(zbior)  # {44, 18, 22, 55}

# użycie sorted() na zbiorze
# zwróci nam listę posortowanych elementów
print(sorted(zbior))  # [18, 22, 44, 55]

# usunięcie elementu ze zbioru
# remove()
zbior.remove(55)
zbior.remove(18)
print(f"Zbiór po usunięciu: {zbior=}")  # Zbiór po usunięciu: zbior={44, 22}
print(f"Zbiór po usunięciu: {zbior}")  # Zbiór po usunięciu: {44, 22}
