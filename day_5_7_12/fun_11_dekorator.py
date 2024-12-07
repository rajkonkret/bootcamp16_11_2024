# dekorator- funkcja opakowująca inn funkcję w dodatkową funkcjonalnosc
# przyjmuje jako argument funkcje
# wykorzystuje zasady funkcji wewnętrznej
def dekor(fun):
    def wew():
        print("Dekoruj")
        return fun()

    return wew


@dekor
def hej():
    print("Hej!!")


hej()  # Hej!!
# po dodaniu dekoratora
# Dekoruj
# Hej!!
