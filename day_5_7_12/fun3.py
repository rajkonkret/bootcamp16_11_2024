a = 10
b = 10


def dodaj():
    a = 6  # zmienne lokalne
    b = 8  # nie zmieniają wartości globalnych
    print(a + b)


def dodaj2():
    print(a + b)  # 20, uzyje wartosci globalnych


def dodaj3():
    global a  # użyj zmiennej globalnej
    a = 5
    b = 8
    print(a + b)


print(f"Zmienna a, b z góry (globalne): {a}, {b}")  # Zmienna a, b z góry (globalne): 10, 10
dodaj()  # 14
print(f"Zmienna a, b z góry (globalne): {a}, {b}")  # Zmienna a, b z góry (globalne): 10, 10
dodaj2()  # 20
print(f"Zmienna a, b z góry (globalne): {a}, {b}")  # Zmienna a, b z góry (globalne): 10, 10
dodaj3()  # 13
print(f"Zmienna a, b z góry (globalne): {a}, {b}")  # Zmienna a, b z góry (globalne): 5, 10
dodaj2()  # 15
