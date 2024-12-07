# funkcja lambda
# skrócony zapis funkcji
# lambda zwraca wynik - return
# funkcja anonimowa - deklaracja w miejscu wykonania

odejmij = lambda a, b: a - b
print(odejmij(6, 8))
print(odejmij(b=6, a=8))
# -2
# 2

addition = lambda a, b: a + b
print(addition(6, 7))
res = addition(7, 8)
print(f'Wynik dodawannia {res}')  # Wynik dodawannia 15

res = lambda *args: sum(args)
print(res(10, 20))  # 30

res = lambda **kwargs: sum(kwargs.values())
print(res(a=10, b=25))  # 35

product = lambda a, b: a * b
print(product(4, 5))  # 20


def product1(nums):
    total = 1
    for i in nums:
        total *= i
    return total


res1 = lambda **kwargs: product1(kwargs.values())
print(res1(a=10, b=90))  # 900


def my_func(n):
    return lambda a: a + n


add10 = my_func(10)
add20 = my_func(20)
add30 = my_func(30)

print(add10(5))  # 15
print(add20(5))  # 25
print(add30(5))  # 35

oblicz_vat = lambda cena, vat=8: cena * (100 + vat) / 100
print(oblicz_vat(1000))
print(oblicz_vat(1000, 23))
print(oblicz_vat(vat=15, cena=1000))  # 1150.0

wiek = lambda x: "dziecko" if x < 10 else ("nastolatek" if x < 18 else "dorosły")
print(wiek(9))  # dziecko
print(wiek(10))  # nastolatek
print(wiek(17))  # nastolatek
print(wiek(18))  # dorosły
print(wiek(25))  # dorosły

# mapowanie
lista = [1, 2, 3, 45, 67, 78, 100, 200, 300]

lista_wyn = []
for i in lista:
    lista_wyn.append(i * 2)
print(lista_wyn)  # [2, 4, 6, 90, 134, 156, 200, 400, 600]

print([i * 2 for i in lista])  # [2, 4, 6, 90, 134, 156, 200, 400, 600]


# print(lista * 2)# [1, 2, 3, 45, 67, 78, 100, 200, 300, 1, 2, 3, 45, 67, 78, 100, 200, 300]

def zmien(x):
    return x * 2


listy_wyn_f = []
for i in lista:
    listy_wyn_f.append(zmien(i))

print(listy_wyn_f)  # [2, 4, 6, 90, 134, 156, 200, 400, 600]

# map() - mapowanie, zmienia dane wg zadanej funkcji
print(f"Zastosowanie map(): {list(map(zmien, lista))}")
# Zastosowanie map(): [2, 4, 6, 90, 134, 156, 200, 400, 600]
# Lambda jako funkcja anonimowa, uzyta w miejscu deklaracji
print(f"Zastosowanie map(): {list(map(lambda x: x * 2, lista))}")
print(f"Zastosowanie map(): {list(map(lambda x: x * 4, lista))}")
print(f"Zastosowanie map(): {list(map(lambda x: x * 12, lista))}")
# Zastosowanie map(): [12, 24, 36, 540, 804, 936, 1200, 2400, 3600]
print(f"Zastosowanie map(): {list(map(lambda x: x * 1.1, lista))}")
# Zastosowanie map(): [1.1, 2.2, 3.3000000000000003, 49.50000000000001,
# 73.7, 85.80000000000001, 110.00000000000001, 220.00000000000003, 330.0]


# filtrowanie danych
# wyciągnie elementu spełniającego warunek
# parzyste
lista_parzyste = []
for i in lista:
    if i % 2 == 0:
        lista_parzyste.append(i)
print(lista_parzyste)  # [2, 78, 100, 200, 300]

# filter()
print(f'Zastosowanie filter() {list(filter(lambda x: x < 3, lista))}')  # Zastosowanie filter() [1, 2]
print(f'Zastosowanie filter() {list(filter(lambda x: x > 15, lista))}')
# Zastosowanie filter() [45, 67, 78, 100, 200, 300]
# x > 5 i x < 200
print(
    f'Zastosowanie filter() {list(filter(lambda x: x > 5 and x < 200, lista))}')  # Zastosowanie filter() [45, 67, 78, 100]
print(f'Zastosowanie filter() {list(filter(lambda x: 5 < x < 200, lista))}')  # Zastosowanie filter() [45, 67, 78, 100]
print(f'Zastosowanie filter() {list(filter(lambda x: x % 2 == 0, lista))}')
# Zastosowanie filter() [2, 78, 100, 200, 300]
