# wyjątki błędy wykonania programu

# print(5 / 0)
# Traceback (most recent call last):
#   File "C:\Users\Administrator\PycharmProjects\bootcamp16_11_2024\day_4_24_11\wyjatki_zad1.py", line 3, in <module>
#     print(5 / 0)
#           ~~^~~
# ZeroDivisionError: division by zero

#  przechwytywanie i obsługa wyjątków
try:
    # print(5 / 0)
    # print("a" / 2)
    # print(int("A"))
    # raise KeyError("Bład klucza")  # rzucenie wyjątku
    wynik = 90 / 3
except ZeroDivisionError:
    print("Nie dziel przezz zero")
except TypeError:
    print('Bład typu')
except ValueError:
    print("Bład wartosci")
except Exception as e:
    print("Błąd", e)
else:  # wykona się tylko gdy nie ma błedu
    print("Wynik", wynik)
finally:  # pojawi się zawsze
    print("Obliczenia wykonane")
print("Program nadal działa")
# Nie dziel przezz zero
# Program nadal działa
# Bład typu
# Program nadal działa
# Wynik 30.0
# Program nadal działa
# Bład wartosci
# Obliczenia wykonane
# Program nadal działa
# Wynik 30.0
# Obliczenia wykonane
# Program nadal działa
