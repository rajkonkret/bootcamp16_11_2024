class Pracownik:
    def __init__(self, imie, nazwisko, pensja):
        self.imie = imie
        self.nazwisko = nazwisko
        self.pensja = pensja

    def przedstwa_sie(self):
        print(f"Czesc, jestem {self.imie} {self.nazwisko}")

    def oblicz_pensje(self):
        return self.pensja


# zrobić klase Manager, dziedziczącą po Pracownik
class Manager(Pracownik):
    """
    klasa Manager
    """

    def __init__(self, imie, nazwisko, pensja, premia):
        super().__init__(imie, nazwisko, pensja)
        self.premia = premia

    def oblicz_pensje(self):
        return self.pensja + self.premia


pracownik = Pracownik("Jan", "Kowalski", 5000)
pracownik.przedstwa_sie()
wyn_prac = pracownik.oblicz_pensje()
print(f"Wynagrodzenie dla pracownika {pracownik.imie} {pracownik.nazwisko}: {wyn_prac}")
# Czesc, jestem Jan Kowalski
# Wynagrodzenie dla pracownika Jan Kowalski: 5000

manago = Manager("Anna", 'Nowak', 10000, 5000)
manago.przedstwa_sie()
wyn_manago = manago.oblicz_pensje()
print(f"Wynagroszenie dla managera {manago.imie} {manago.nazwisko}: {wyn_manago}")
# Czesc, jestem Anna Nowak
# Wynagroszenie dla managera Anna Nowak: 15000
