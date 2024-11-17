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

# tworzenie zbioru z konkretnymi elementami
zbior2 = {667, 11, 44, 18, 52, 22, 667, 62, 999}
print(zbior2)  # {999, 11, 44, 18, 52, 22, 667, 62}

zbior_3 = {667, 11, 44, 18, 667, 62, 999}
# suma zbiorów - wszystkie elementy, które znajdują sie w jednym i drugim zbiorze
# tworzy nowy zbiór
print(zbior | zbior_3)  # {999, 11, 44, 18, 22, 667, 62}
print(zbior.union(zbior_3))  # {999, 11, 44, 18, 22, 667, 62}
# zbiory bazowe nie zmieniły się
print(zbior)  # {44, 22}
print(zbior_3)  # {18, 999, 11, 44, 667, 62}
zbior_4 = {8, 9, 10}
print(zbior.union(zbior_3, zbior_4))
# {999, 8, 9, 10, 11, 44, 18, 22, 667, 62} - suma trzech zbiorów
print(zbior | zbior_3 | zbior_4)
# {999, 8, 9, 10, 11, 44, 18, 22, 667, 62}

# część wspólna - zwraca nowy zbiór
print(zbior & zbior_3)  # {44}
print(zbior.intersection(zbior_3))  # {44}

# róznica zbiorów
print(zbior - zbior_3)  # {22}
print(zbior.difference(zbior_3))  # {22}
print(zbior_3.difference(zbior))  # {999, 11, 18, 667, 62}

zbior_copy = zbior.copy()
print(zbior_copy)  # {44, 22}
zbior.clear()  # usunięcie elementów ze zbioru
print(zbior)  # set() - pusty zbiór
print(zbior_copy)  # {44, 22}

# suma zbiorów
# zmienia zbiór bazowy
# wynik łączenia w zbiorze a
a = {1, 2}
b = {2, 3}
a.update(b)
print(a)  # {1, 2, 3}

a = {1, 2, 3}
b = {2, 3, 4}
a.intersection_update(b)  # część wspólna le zmieni się zawartość zbioru a
print(a)  # zbiór a zostanie nadpisany elementami wspólnymi, {2, 3}

# frozenset() - zbiór niemutowalny
frozen = frozenset([1, 2, 3])
print(frozen)  # frozenset({1, 2, 3})

lista_temp = [[2, 3], [4, 5]]
print(lista_temp)  # [[2, 3], [4, 5]]

# nie da się robić zagnieżdzonych zbiorów
# nested_set = {1, {2, 3}} # TypeError: unhashable type: 'set'

nested_set = {1, frozenset({2, 3})}
print(nested_set)  # {1, frozenset({2, 3})}

zb3 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(sum(zb3))  # 45, suma elementów zbioru
print(max(zb3))  # 9 wartość maksymalna
print(min(zb3))  # wartość minimalna
print(len(zb3))  # długosć zbioru 9
print(sorted(zb3))  # zwróci listę, [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Czy zbiór b jest podzbiorem zbioru a? issubset()
a = {1, 2, 3}
b = {1, 2}
print(b.issubset(a))  # True
