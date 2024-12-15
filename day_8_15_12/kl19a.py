# wyjątki
# możemy dziedziczyć po klasie Exception i tworzyc swoje wyjątki
class MyException(Exception):
    def __init__(self, message):
        super().__init__(message)


# print(2 / 0) # ZeroDivisionError: division by zero
# raise ZeroDivisionError("Nie dziel przez zero") # ZeroDivisionError: Nie dziel przez zero

try:
    x = int(input("Podaj liczbę całkowitą dodatnią"))
    if x < 0:
        print("Liczba ma być większa od zera")
        raise MyException("Liczba musi być dodatnia")
except MyException:
    print("Wystąpił wyjątek MyException")
except ValueError:
    print("Wystąpił błąd wartości")
except Exception as e:
    print("Bład inny", e)
else:
    print("Wprowadziłeś poprawną wartość", x)
finally:
    print("Wprowadź kolejne dane")
# Podaj liczbę całkowitą dodatnią-9
# Liczba ma być większa od zera
# Wystąpił wyjątek MyException
