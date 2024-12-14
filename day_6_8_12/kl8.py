# klasa abstrakcyjna -
# klasa z kórej nie można zrobić obiektu
# metoda abstrakcyjba @abstactmethod
from abc import ABC, abstractmethod


class Ptak(ABC):
    """
    Klasa opisująca ptaka w Pythonie
    """

    def __init__(self, gatunek, szybkosc):
        self.gatunek = gatunek
        self.szybkosc = szybkosc

    def latam(self):
        print("Tu", self.gatunek, "Lecę z szybkością", self.szybkosc)

    @abstractmethod  # metoda abstrakcyjna
    def wydaj_odglos(self):
        pass


class Kura(Ptak):
    def __init__(self, gatunek):
        super().__init__(gatunek, 0)  # prędkość zawsze ustawiamy na 0 dla kury

    def latam(self):
        print("Tu", self.gatunek, "Ja nie latam")

    def wydaj_odglos(self):
        print("Ko ko ko ko ko")

    def dziobanie(self):
        print("Tu", self.gatunek, "Idę sobie podziobać")


class Orzel(Ptak):
    """
    klasa Orzel
    """

    def wydaj_odglos(self):
        print("Kier kir kier")

    def polowanie(self):
        print('Tu', self.gatunek, "Rozpoczynam polowanie")


# TypeError: Can't instantiate abstract class Ptak without an implementation for abstract method 'wydaj_odglos'
# nie mozna tworzyc obiektu tej klasy - klasa abstrakcyjna
# or1 = Ptak("Orzeł", 45)
# or1.latam()  # Tu Orzeł Lecę z szybkością 45
# kur1 = Ptak("Kura", 0)
# kur1.latam()  # Tu Kura Lecę z szybkością 0

kur2 = Kura("Kura domowa")
kur2.latam()  # Tu Kura domowa Ja nie latam
or2 = Orzel("Orzel bielik", 50)
or2.latam()
# Tu Kura domowa Ja nie latam
# Tu Orzel bielik Lecę z szybkością 50

or2.wydaj_odglos()
kur2.wydaj_odglos()
# Kier kir kier
# Ko ko ko ko ko

or2.polowanie()
kur2.dziobanie()
# Tu Orzel bielik Rozpoczynam polowanie
# Tu Kura domowa Idę sobie podziobać

# polimorfizm - obiekty róznych klas mają wspolne cechy
# klasa abstrakcyjna mocniej je akcentuje
lista = [or2, kur2]
for i in lista:
    print(i.__class__.__name__, i.wydaj_odglos())
# Kier kir kier
# Orzel None
# Ko ko ko ko ko
# Kura None
