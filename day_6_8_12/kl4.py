# napisac kalsę Dom
# ma posiadac pola prywatne kolor, liczba okien, metraz
# doac metody do odczytu tych pol
class Dom:
    """
    klasa opisująca dom
    """

    def __init__(self, metraz, kolor, liczba_okien):
        self.__metraz = metraz
        self.__kolor = kolor
        self.__liczba_okien = liczba_okien

    def wyswietl_okna(self):
        print(f"Mam {self.__liczba_okien} okna/okien")

    def wyswietl_kolor(self):
        print(f"Mam kolor: {self.__kolor}")

    def wyswietl_metraz(self):
        print(f"Mam metraz: {self.__metraz}")


dom1 = Dom(200, "czerwony", 11)
dom1.wyswietl_metraz()
dom1.wyswietl_kolor()
dom1.wyswietl_okna()
# Mam metraz: 200
# Mam kolor: czerwony
# Mam 11 okna/okien