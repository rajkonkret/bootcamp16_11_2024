import sys

wiek = 47  # int
rok = 2024  # int
temp = 36.6  # float

print(temp)
print(type(temp))  # <class 'float'>

print(wiek + rok)  # 2071
print(wiek - rok)  # -1977
print(wiek * rok)  # 95128
print(wiek / rok)  # 0.023221343873517788

print(rok // wiek)  # częśc całkowita z dzielenia, 43
print(5 // 2)  # 2

print(rok % wiek)  # modulo, reszta z dzielenia 3
print(3 % 2)  # 3 //2 = 1 to 1 * 2 = 2, reszta 3 - 2 = 1

print(wiek ** rok)
print(f"{wiek ** rok:,}")

wynik = wiek ** rok
print(len(str(wynik)))  # długość 3385 cyfr
# print(len(str(wynik ** 2))) #
# ValueError: Exceeds the limit (4300 digits) for integer string conversion;
# use sys.set_int_max_str_digits() to increase the limit

print(74 - 8 * 45 + 8 / 2 + 8 / 2)  # -278.0
print(74 - (8 * 45) + 8 / 2 + 8 / 2)  # -278.0
print(74 - (8 * 45) + (8 / 2 + 8) / 2)  # -280.0

# liczby float
# liczby zmiennoprzecinkowe
print(0.2 + 0.8)  # float 1.0
print(0.2 + 0.7)  # 0.8999999999999999
print(0.1 + 0.2)  # 0.30000000000000004
# 12.345 + 1.0001 = 13.3451 might be rounded to 13.345.
# float jest zapamiętywany w komputerze w sposób wykładniczy
# a * 2 ^ n
# z tego wynika bład zaokraglenia
print(f"{0.2 + 0.7:.1f}")  # 0.9
print(sys.float_info)
# sys.float_info(
#     max=1.7976931348623157e+308,
#     max_exp=1024,
#     max_10_exp=308,
#     min=2.2250738585072014e-308,
#     min_exp=-1021,
#     min_10_exp=-307,
#     dig=15,
#     mant_dig=53
#     , epsilon=2.220446049250313e-16, radix=2, rounds=1)

print(f"Sprawdzenie zmiennej temp {temp}, wiek {wiek}")
# Sprawdzenie zmiennej temp 36.6, wiek 47

print(f'''
    {wiek}
    {temp}
''')
# "
#     47
#     36.6"

print(type(4 / 2))  # zawsze daje <class 'float'>
print(4 / 2)  # 2.0

# typy prymitywne - str, int, float, bool, bytes
# typ logiczny, boolean, bool
# prawda, fałsz -> True, False
# 1 - prawda, 0 - fałsz

czy_znasz_pythona = True
print(czy_znasz_pythona)  # True
print(type(czy_znasz_pythona))  # <class 'bool'>, typ logiczny

print(int(czy_znasz_pythona))  # 1
czy_znasz_pythona = False
print(int(czy_znasz_pythona))  # 0

x = 1
print(bool(x))  # True
x = 0
print(bool(x))  # False

x = 100
print(bool(x))  # True
x = -10
print(bool(x))  # True
x = "radek"
print(bool(x))  # True

x = ""
print(bool(x))  # False
x = None  # nic, stan nieokreślony - odpowiednik null

print(bool(x))  # False# porówanie elementów daje w wyniku typ logiczny
a = 14
b = 3

print(f"Wynik porównania {a} > {b} = {a > b}")  # Wynik porównania 14 > 3 = True
print(f"Wymik porównania {a > b = }")  # Wymik porównania a > b = True
print("Wynik porównania", a, "<", b, "=", a < b)  # Wynik porównania 14 < 3 = False
print(f"Wynik porównania {a} < {b} = {a < b}")  # Wynik porównania 14 < 3 = False
print(f"Wynik porównania {a} <= {b} = {a <= b}")  # Wynik porównania 14 <= 3 = False
print(f"Wynik porównania {a} >= {b} = {a >= b}")  # Wynik porównania 14 >= 3 = True

print(f"Wynik porównania {a} == {b} = {a == b}")  # == porównanie, Wynik porównania 14 == 3 = False
print(f"Wynik porównania {a} != {b} = {a != b}")  # != czy różne, Wynik porównania 14 != 3 = True

# operacje logiczne
# and - i
print(True and True)  # True
print(True and False)  # False
print(False and True)  # False
print(False and False)  # False

# or - lub
print(True or True)  # True
print(True or False)  # True
print(False or True)  # True
print(False or False)  # False

# not - negacja
print(not True)  # False
print(not False)  # True

my_str = '123456789'
# A string is numeric if all characters in the string are numeric
print(my_str.isnumeric())  # True
#  A string is alpha-numeric if all characters in the string are alpha-numeric
print(my_str.isalnum())  # True
# A string is a decimal string if all characters in the string are decimal
print(my_str.isdecimal())  # True
#  A string is alphabetic if all characters in the string are alphabetic
print(my_str.isalpha())  # False

print("------")
my_str = "abcdefghijkl"
print(my_str.isalpha())  # True
print(my_str.isalnum())  # True
print(my_str.isdecimal())  # False
print(my_str.isnumeric())  # False
print(my_str.islower())  # True
print(my_str.isupper())  # False

my_str3 = "Radek12345"
print(my_str3.isalpha())  # False
print(my_str3.isalnum())  # True
print(my_str3.isdecimal())  # False
print(my_str3.isnumeric())  # False
print(my_str3.islower())  # False
print(my_str3.isupper())  # False
