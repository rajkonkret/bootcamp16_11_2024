# klasa - szablon, wzór, przepis
# obiekt - zbudowny wg przepisu, instancja
# enkapsulacja, hermetyzacja, abstrakcja, dziedziczenie, polimorfizm
# pola, funkcje
# klasa musi byc najpierw zadeklarowana
# obiekt uruchamia elementy klasy

class Human:
    """
    Klasa Human opisująca człowieka w pythonie
    """
    imie = ""
    wiek = None
    plec = "k"

    def powitanie(self):  # self = cz2
        print(f"Nazywam się {self.imie}")

    # wypisz_wiek()
    def wypisz_wiek(self):
        print(f"Mam {self.wiek} lat.")


print(Human.__doc__)  # Klasa Human opisująca człowieka w pythonie
print(print.__doc__)
# cd .\day_6_8_12\ - zmiana katalogu
# pydoc -b uruchumienie serwera z dokumentacją
# pydoc -w kl1 - stworzenie pliku html z dokumentacją dla danego pliku pythona
cz1 = Human()  # tworzenie obiekty klasy
print(cz1.imie)
print(cz1.wiek)
print(cz1.plec)
#
# None
# k

cz1.imie = "Radek"
cz1.plec = "m"
cz1.wiek = 78
print(cz1.imie)
print(cz1.wiek)
print(cz1.plec)
# Radek
# 78
# m
cz2 = Human()
cz2.imie = "Ania"
cz2.plec = "k"
cz2.wiek = 38
print(cz2.imie)
print(cz2.wiek)
print(cz2.plec)
# Ania
# 38
# k
cz1.powitanie()
cz2.powitanie()
# Nazywam się Radek
# Nazywam się Ania
cz1.wypisz_wiek()
cz2.wypisz_wiek()
# Mam 78 lat.
# Mam 38 lat.