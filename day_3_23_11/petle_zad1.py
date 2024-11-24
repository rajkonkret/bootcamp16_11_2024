# pętla - możliwość wykonania tego samego fragmentu kodu wielokrotnie
# for - pętla iteracyjna
import random
from itertools import zip_longest

for i in range(10):  # od 0 do 9
    print(i)

for i in range(10):  # od 0 do 9
    print(i, i, sep=":")  # 9:9

for i in range(10):
    print(i, end="")  # 0123456789, wszystko wypisane w jednej linii

print()  # ustawienie end="\n"
print("Konniec pętli")  # Konniec pętli

for i in range(1, 25):  # od 1 do 24
    print(i)

for _ in range(1, 5):  # _ niema zmienna
    print("Kominkat")
    # print(_)

my_string = "Radek"
for i in my_string:  # petla działa, aż skończą się w niej elementy
    print(i)

# przerobic lotto na pętle
print("----------------")
lista_kule = list(range(1, 50))
lista_wylosowane = []

for _ in range(6):
    wyn = random.choice(lista_kule)
    lista_kule.remove(wyn)
    # print(wyn)
    lista_wylosowane.append(wyn)

print(lista_wylosowane)  # [48, 38, 17, 8, 18, 7]

# posortowac liste wyników
lista_wylosowane.sort()
print(lista_wylosowane)
# [46, 12, 7, 10, 45, 49]
# [7, 10, 12, 45, 46, 49]

for i in range(10):
    if i % 2 == 0:  # % modulo, reszta z dzielenia
        print(i, "parzysta")
# 0 parzysta
# 2 parzysta
# 4 parzysta
# 6 parzysta
# 8 parzysta

# list comprehension
lista3 = [j for j in range(1, 10) if j % 2 == 0]
print(lista3)  # [2, 4, 6, 8]

for c in lista3:
    if c == 2:
        c += 1  # c = c + 1
        print("Tylko jeśli c=2")
    print("Przy każdym elemencie pętli", c)
# [2, 4, 6, 8]
# Tylko jeśli c=2
# Przy każdym elemencie pętli 3
# Przy każdym elemencie pętli 4
# Przy każdym elemencie pętli 6
# Przy każdym elemencie pętli 8

a = 1
a += 1  # a = a + 1
print(a)  # 2
a -= 1  # a = a - 1
print(a)  # 1
a *= 2  # a = a * 2
print(a)  # 2
a /= 2  # a = a / 2
print(a)  # 1.0 float
a %= 2
print(a)  # 1.0

imiona = ['Radek', 'Tomek', "Zenek", "Zbyszek"]
for p in imiona:
    print(p)
# Radek
# Tomek
# Zenek
# Zbyszek

print(p)  # Zbyszek, globalne zmienna

# wyświetlic z listy
# 0 Radek
for i in range(len(imiona)):  # range(4) -> 0...3
    print(i, imiona[i])
# 0 Radek
# 1 Tomek
# 2 Zenek
# 3 Zbyszek

for p in imiona:
    print(imiona.index(p), p)
# 0 Radek
# 1 Tomek
# 2 Zenek
# 3 Zbyszek

# enumerate() - zwraca element kolekcji i jego pozycję
for i in enumerate(imiona):
    print(i)
# (0, 'Radek')
# (1, 'Tomek')
# (2, 'Zenek')
# (3, 'Zbyszek')
a, b = (0, 'Radek')  # rozpakowanie krotki
print(a, b)

for pozycja, osoba in enumerate(imiona):
    print(pozycja, osoba)
# 0 Radek
# 1 Tomek
# 2 Zenek
# 3 Zbyszek

for p, o in enumerate(imiona, start=1):
    print(p, o)
# 1 Radek
# 2 Tomek
# 3 Zenek
# 4 Zbyszek

ludzie = ['Radek', 'Janek', "Tomek", "Marek"]
wiek = [45, 40, 18, 23]
# wypisaniu w takiej formie Radek 45

for i in range(len(ludzie)):
    print(ludzie[i], wiek[i])
# Radek 45
# Janek 40
# Tomek 18
# Marek 23

ludzie = ['Radek', 'Janek', "Tomek", "Marek", "Ania"]
wiek = [45, 40, 18, 23]
# for i in range(len(ludzie)):
#     print(ludzie[i], wiek[i]) # IndexError: list index out of range

# zip() - łączenie kolekcji
for i in zip(ludzie, wiek):
    print(i)
# ('Radek', 45)
# ('Janek', 40)
# ('Tomek', 18)
# ('Marek', 23)
for l, w in zip(ludzie, wiek):
    print(l, w)
# Radek 45
# Janek 40
# Tomek 18
# Marek 23

# 0 Radek 45
for i in enumerate(zip(ludzie, wiek)):
    print(i)
# (0, ('Radek', 45))
# (1, ('Janek', 40))
# (2, ('Tomek', 18))
# (3, ('Marek', 23))
a, b = (0, ('Radek', 45))
print(a, b)  # 0 ('Radek', 45)
c, d = ('Radek', 45)
print(c, d)  # Radek 45
(i, (l, w)) = (0, ('Radek', 45))  # nawiasy wskazują wewnętrzną krotkę
print(i, l, w)  # 0 Radek 45
for i, (l, w) in enumerate(zip(ludzie, wiek)):
    print(i, l, w)
# 0 Radek 45
# 1 Janek 40
# 2 Tomek 18
# 3 Marek 23

zipped = zip_longest(ludzie, wiek, fillvalue="NONE")
print(type(zipped))  # <class 'itertools.zip_longest'>
zipped_tuple = tuple(zipped)
print(zipped_tuple)  # (('Radek', 45), ('Janek', 40), ('Tomek', 18), ('Marek', 23), ('Ania', 'NONE'))
# iterator - pozwala na asekwencyjne dostęp do danych
# po odczytaniu danych  nie są już dostępne
# Pętle po zipped nie odczytają danych
for i in zipped:
    print(i)
# ('Radek', 45)
# ('Janek', 40)
# ('Tomek', 18)
# ('Marek', 23)
# ('Ania', 'NONE')

print("----------")
for o, w in zipped:
    print(o, w)

print("*" * 25)
for i in zipped_tuple:
    print(i)
# (('Radek', 45), ('Janek', 40), ('Tomek', 18), ('Marek', 23), ('Ania', 'NONE'))
# ----------
# *************************
# ('Radek', 45)
# ('Janek', 40)
# ('Tomek', 18)
# ('Marek', 23)
# ('Ania', 'NONE')
for name, age in zipped_tuple:
    print(name, age)
# Radek 45
# Janek 40
# Tomek 18
# Marek 23
# Ania NONE

for i in range(0, 10, 2):  # (start, stop, krok)
    print(i)
# 0
# 2
# 4
# 6
# 8
for i in range(-10, 0, 2):
    print(i)
# -10
# -8
# -6
# -4
# -2

for i in range(10, 0, -2):  # krok ujemny, krok w tył(dół)
    print(i)
# 10
# 8
# 6
# 4
# 2

parzyste = [i for i in range(0, 10, 2)]
print(parzyste)  # [0, 2, 4, 6, 8]

ang_pol = {'name': 'imie', 'cat': 'kot', 'water': "woda"}
pol_ang = {}
print(ang_pol.items())  # dict_items([('name', 'imie'), ('cat', 'kot'), ('water', 'woda')])
for k, v in ang_pol.items():
    pol_ang[v] = k
print(pol_ang)  # {'imie': 'name', 'kot': 'cat', 'woda': 'water'}

print({v: k for k, v in ang_pol.items()})  # {'imie': 'name', 'kot': 'cat', 'woda': 'water'}
