# # liczby float
# # liczby zmiennoprzecinkowe
# print(0.2 + 0.8)  # float 1.0
# print(0.2 + 0.7)  # 0.8999999999999999
# print(0.1 + 0.2)  # 0.30000000000000004
# # 12.345 + 1.0001 = 13.3451 might be rounded to 13.345.
# # float jest zapamiętywany w komputerze w sposób wykładniczy

# decimal - typ liczbowy pozwalający zarządzać zaokrgleniem w taki sposób aby wyeliminować problem zaokrąglenia
# jaki występuje w liczbach float
# decimal wolniejsze obliczenia, zużywa więcej pamięci
from decimal import Decimal, ROUND_HALF_UP

# tworzenie liczb
decimal_1 = Decimal("0.1")
decimal_2 = Decimal(0.1)
decimal_3 = Decimal(1)

# wypisywanie
print(decimal_1)
print(decimal_2)
print(decimal_3)
# 0.1
# 0.1000000000000000055511151231257827021181583404541015625
# 1

# porównanie
print(f"Decimal('0.1') == Decimal(0.1)? {decimal_1 == decimal_2}")  # Decimal('0.1') == Decimal(0.1)? False
print(f"Decimal('0.1') == Decimal('0.1')? {decimal_1 == Decimal('0.1')}")  # Decimal('0.1') == Decimal('0.1')? True
print(f"Decimal(1) == Decimal('1')? {decimal_3 == Decimal('1')}")  # Decimal(1) == Decimal('1')? True

# operacje matematyczne decimal
a = Decimal('10.345')
b = Decimal("3.2")

add = a + b
print("Dodawanie", add)
substract = a - b
print("Odejmowanie", substract)
multiply = a * b
print("Mnożenie", multiply)
divide = a / b
print("Dzielenie", divide)
# Dodawanie 13.545
# Odejmowanie 7.145
# Mnożenie 33.1040
# Dzielenie 3.2328125

# z zaokrągleniem do dwóch mmiejsc po przecinku
print("Liczby zaokrąglone do dwóch miejsc po przecinku")
add = add.quantize(Decimal("0.01"))
print("Dodawanie", add)
substract = substract.quantize(Decimal("0.01"))
print("Odejmowanie", substract)
multiply = multiply.quantize(Decimal("0.01"))
print("Mnożenie", multiply)
divide = divide.quantize(Decimal("0.01"))
print("Dzielenie", divide)
# Liczby zaokrąglone do dwóch miejsc po przecinku
# Dodawanie 13.54
# Odejmowanie 7.14
# Mnożenie 33.10
# Dzielenie 3.23

divide = a / b
print("Dzielenie z ustawieniem zaokrąglania", divide.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))
# ROUND_DOWN: Final[str]
# ROUND_HALF_UP: Final[str]
# ROUND_HALF_EVEN: Final[str]
# ROUND_CEILING: Final[str]
# ROUND_FLOOR: Final[str]
# ROUND_UP: Final[str]
# ROUND_HALF_DOWN: Final[str]
# ROUND_05UP: Final[str]

value = Decimal("5.456")
rounding_nearest_005 = (value / Decimal("0.05")).quantize(Decimal("1"), rounding=ROUND_HALF_UP) * Decimal("0.05")
print(rounding_nearest_005)
print(Decimal("1.01") + 9)  # 10.01
