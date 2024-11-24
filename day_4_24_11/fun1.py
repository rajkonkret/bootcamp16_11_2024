# funkcje - wydzielony fragment programu wykonac w dowolnym momencie
# funkcja przed użyciem musi zostać zdefiniowana
# w miejscu definicji funkcja się nie wykonuje
# aby funkcja się uruchomiła musimy ją wywołać


# te funkcje nie zwracają wyniku
# zmienne globalne
# widoczne również wewnątrz funkcji
a = 6
b = 8


# PEP8 zaleca by definicja funkcji była oddzielona od reszty programu dwoma pustymi linijkami
# definicja funkcji
def dodaj():  # funkcja bezargumentowa
    print(a + b)
    c = 7  # to jest zmienna lokalna tylko dla tej funkcji


# funkcja z argumentami a i b
def dodaj2(a, b):
    # zaciemniliśmy widoczność globalnych, musimy obowiązkowo przekazac a i b
    # a i b mają zasięg lokalny
    print(a + b)


# c=0 argument o wartości domyślnej
def odejmij(a, b, c=0):
    print(a - b - c)


# wywołanie funkcji
# nazwa funkcji i nawiasy ()
print(dodaj)  # wypisze adres funkcji dodaj <function dodaj at 0x0000020AF4668A40>
print(type(dodaj))  # <class 'function'> funkcja
dodaj()  # uruchomienie funkcji, 14
# print(c)  # NameError: name 'c' is not defined

## argumenty pozycyjne, po kolei trafia do kolejnych argumentów w funkcji
# musimy obowiązkowo przekazać dwa argumnty, zostaną podstawione do a i b w funkcji dodaj2
# dodaj2()  # TypeError: dodaj2() missing 2 required positional arguments: 'a' and 'b'
dodaj2(10, 67)  # 77

# funkcja odejmij ma argument domyślny
# pozwala to ominąc brak możliwości
# przeciązania funkcji liczb argumentów
odejmij(1, 2)  # c=0, -1
odejmij(1, 2, 3)  # c=3, -4

## argumenty przekazane po nazwie
odejmij(c=9, a=9, b=88)  # -88
odejmij(b=67, a=78)  # 11
dodaj2(b=7, a=9)  # 16

# mieszane
odejmij(1, c=90, b=87)  # -176
odejmij(1, b=87)  # -86
dodaj2(3, b=89)  # 92

# nie można przekazywac argumentów pozycyjnych po nazwanych
# odejmij(c=90, 3, 4) # SyntaxError: positional argument follows keyword argument

print("-----------")
print(dodaj())
# 14
# None

# print(dodaj() + dodaj())  # TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'
# jesli funkcja nie zwraca wyniku nie możemy tego wyniku dalej użyć
