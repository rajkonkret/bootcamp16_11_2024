class Human:
    """
    Klasa Human opisująca człowieka w pythonie
    """

    def __init__(self, imie, wiek, wzrost, plec='k'):
        """
        Metoda inicjalizująca (konstruktor)
        :param imie:
        :param wiek:
        :param wzrost:
        :param plec:
        """
        self.imie = imie
        self.wiek = wiek
        self.wzrost = wzrost
        self.plec = plec

    def powitanie(self):  # self = cz2
        print(f"Nazywam się {self.imie}")

    def wypisz_wiek(self):
        print(f"Mam {self.wiek} lat.")

    def wypisz_wzrost(self):
        print(f"Mam {self.wzrost} cm wzrostu.")

    def ruszaj(self):
        if self.plec == "m":
            print("Ruszyłem w droge")
        else:
            print("Ruszyłam w drogę")


# cz1 = Human() # TypeError: Human.__init__() missing 3 required positional arguments: 'imie', 'wiek', and 'wzrost'
cz1 = Human("Ania", 34, 165)
print(cz1.wiek)  # 34
print(cz1.wzrost)  # 165
print(cz1.imie)  # Ania
print(cz1.plec)  # k

cz2 = Human("Radek", 45, 193, "m")
print(cz1.__doc__)  # Klasa Human opisująca człowieka w pythonie

cz1.powitanie()
cz2.powitanie()

cz1.wypisz_wzrost()
cz2.wypisz_wzrost()

cz1.wypisz_wiek()
cz2.wypisz_wiek()
# Nazywam się Ania
# Nazywam się Radek
# Mam 165 cm wzrostu.
# Mam 193 cm wzrostu.
# Mam 34 lat.
# Mam 45 lat.

cz1.ruszaj()  # Ruszyłam w drogę
cz2.ruszaj()  # Ruszyłem w droge
