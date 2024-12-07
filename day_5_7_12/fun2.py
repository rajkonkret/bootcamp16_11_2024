# funkcje zwracajce wynik
# muszą byc zakończone return

def odejmij(a, b):
    return a - b  # funkcja zwraca wynik


def odejmij2(a=0, b=0, c=0):
    return a - b - c


def oblicz_vat(cena, vat=23):
    return cena * (100 + vat) / 100  # float


# 6 - 9  = -3

print(odejmij(6, 9))  # -3
wynik = odejmij(6, 9)
print("Wynik", wynik)  # Wynik -3

print(odejmij2())  # 0
print(odejmij2(5, 6))  # -1
print(odejmij2(6, 3, 4))  # -1
print(odejmij2(b=8, a=9))  # 1
print(odejmij2(1, c=8, b=5))  # -12

print(odejmij(6, 9) + odejmij2(100, 23, 4))  # 70

print(oblicz_vat(1000))  # float, 1230.0
va1 = oblicz_vat(1000)
if va1 == 1230:
    print("Działa")  # Działa
