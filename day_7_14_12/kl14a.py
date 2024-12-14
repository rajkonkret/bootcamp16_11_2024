class Matematyka:

    @staticmethod
    def dodaj(a, b):
        return a + b

    @staticmethod
    def odejmij(a, b):
        return a - b


# mat = Matematyka()
wynik = Matematyka.dodaj(5, 6)  # 11
print(wynik)
wynik = Matematyka.odejmij(65, 34)  # 31
print(wynik)


# klasa z metodami statycznymi
# celcjusz na frenheit
# farenheit na celcjusz

class KalkulatorTempertur:

    @staticmethod
    def celcius_to_farenheit(celcius):
        return celcius * 9 / 5 + 32

    @staticmethod
    def fahrenheit_to_celcius(farenheit):
        return (farenheit - 32) * 5 / 9


print(KalkulatorTempertur.fahrenheit_to_celcius(100))  # 37.77777777777778
print(KalkulatorTempertur.celcius_to_farenheit(2))  # 35.6
print(KalkulatorTempertur.celcius_to_farenheit(37.77777777777778))  # 100.0
assert 100.0 == KalkulatorTempertur.celcius_to_farenheit(37.77777777777778)
# assert 100.0 == KalkulatorTempertur.celcius_to_farenheit(37.77777777777777)
#     assert 100.0 == KalkulatorTempertur.celcius_to_farenheit(37.77777777777777)
#            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# AssertionError
