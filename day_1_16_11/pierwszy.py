# PEP8 - https://peps.python.org/pep-0008/
# PEP 8 – Style Guide for Python Code
# https://kariera.comarch.pl/blog/clean-code-15-krokow-do-stworzenia-czystego-kodu/
# snake_case - konwencja nazewnicza dla nazw plikó, zmiennych, funkcji
import sys

print()  # wydrukuj/wypisz
# ctrl alt l - formatowanie kodu wg zasad PEP8

print("Nazywam się Radek")  # Nazywam się Radek
print('Nazywam się Radek')  # Nazywam się Radek
print('Nazywam się Radek')  # Nazywam się Radek
print('Nazywam się Radek')  # Nazywam się Radek
print('Nazywam się Radek')  # Nazywam się Radek
print('Nazywam się Radek')  # Nazywam się Radek
# ctrl d - powielenie linii
# print('Nazywam się Zenek")
#   File "C:\Users\Administrator\PycharmProjects\bootcamp16_11_2024\day_1_16_11\pierwszy.py", line 16
#     print('Nazywam się Zenek")
#           ^
# SyntaxError: unterminated string literal (detected at line 16)
# Process finished with exit code 1 - program zakończył się z błędem
# ctrl / - komentarz zaznaczonych linijek

# type() - sprawdzenie typu danych
print(type("Radek"))  # <class 'str'>, string, dane typu tekstowego

print("39" + "14")  # konkatenacja, łaczenie stringów, 3914

print(39)
print(type(39))  # <class 'int'>, integer - liczby calkowite

# print("39" + 14) # TypeError: can only concatenate str (not "int") to str
# silne typowanie - sam nie zamienia typów

print("39" + str(14))  # str() zamiana (rzutowanie) na string, 3914

print(int("39") + 14)  # int() - rzutowanie na int, 53

print(5 * "4")  # 44444
print(35 * "168")
# 168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168168
print(35 * 168)  # 5880
print(int("35") * int(168))  # 5880

print(sys.int_info)
# sys.int_info(
# bits_per_digit=30,
# sizeof_digit=4,
# default_max_str_digits=4300,
# str_digits_check_threshold=640)
# int w python 64 bitowym ograniczony jest pamięcią
