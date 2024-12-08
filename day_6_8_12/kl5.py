# dziedziczenie
class Pojazd:
    def __init__(self, kolor):
        self.kolor = kolor

    def info(self):
        print(f"Kolor: {self.kolor}")


class Samochod(Pojazd):
    """
    Klasa Samochód, dziedziczy po klasie Pojazd
    """

    def __init__(self, kolor, marka="Fiat"):
        super().__init__(kolor)  # obowiązkowo musimy wywołac konstruktor z klasy wyzszej super()
        self.marka = marka

    def info(self):
        super().info()  # mozęmy wywołac metode z klasy super()
        print(f"Marka: {self.marka}")


class Rower(Pojazd):
    """
    Klasa Rower
    """


poj = Pojazd("czerwony")
poj.info()  # Kolor: czerwony

sam = Samochod("zielony")
sam.info()  # Kolor: zielony
# po nadpisaniu __init__ i info()
# Kolor: zielony
# Marka: Fiat

rower = Rower("Zółty")
rower.info()  # Kolor: Zółty

lista = [poj, sam, rower]
print(lista)
# [<__main__.Pojazd object at 0x0000029A4330A2D0>,
# <__main__.Samochod object at 0x0000029A432DCE00>,
# <__main__.Rower object at 0x0000029A430075C0>]

# obiekty róznych klas
# mają wspólną metodę info()
# polimorfizm - obiekty róznych klas traktowane jak jednej.
for i in lista:
    print(i.__class__.__name__)
    i.info()
# Pojazd
# Kolor: czerwony
# Samochod
# Kolor: zielony
# Marka: Fiat
# Rower
# Kolor: Zółty
