# funkcja, która oblicza średnią ocen
def srednia(name=None, *cyfry):  # * dowolna ilosć argumentów pozycyjnych
    print(cyfry)
    count = len(cyfry)
    suma = 0
    sum_p = sum(cyfry)
    try:
        for c in cyfry:
            suma += c

        avg = suma / count
        avg_p = sum_p / count
    except Exception as e:
        print("Błąd", e)
    else:
        print(f"Średnia dla ucznia {name} wynosi {avg}")
        print(f"Średnia dla ucznia {name} wynosi {avg_p}")
    finally:
        print("Następne obliczenie")


srednia()  # () - krotka, tuple, Błąd division by zero
srednia(1)  # (1,)
srednia(1, 2, 3, 4)  # (1, 2, 3, 4)
srednia(1, 2, 3, 4, 5, 6)  # (1, 2, 3, 4, 5, 6)
srednia("a", 1, 2, 3, 4, 5, 6)  # (1, 2, 3, 4, 5, 6), Błąd unsupported operand type(s) for +=: 'int' and 'str'

# ()
# Błąd division by zero
# Następne obliczenie
# ()
# Błąd division by zero
# Następne obliczenie
# (2, 3, 4)
# Średnia dla ucznia 1 wynosi 3.0
# Następne obliczenie
# (2, 3, 4, 5, 6)
# Średnia dla ucznia 1 wynosi 4.0
# Następne obliczenie
# (1, 2, 3, 4, 5, 6)
# Średnia dla ucznia a wynosi 3.5
# Następne obliczenie

# Średnia dla ucznia a wynosi 3.5
# Średnia dla ucznia a wynosi 3.5
# Następne obliczenie
