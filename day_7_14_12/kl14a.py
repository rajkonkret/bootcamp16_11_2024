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
