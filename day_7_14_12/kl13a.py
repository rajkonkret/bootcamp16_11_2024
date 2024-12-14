class MyClass:
    counter = 0

    @classmethod
    def increment_counter(cls):
        cls.counter += 1
        return cls.counter


print(MyClass.increment_counter())
print(MyClass.increment_counter())
print(MyClass.increment_counter())
c = MyClass()
print(c.increment_counter())  # 4


class Osoba:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    @classmethod
    def z_nazwy_pelne(cls, nazwa_pelna):
        imie, nazwisko = nazwa_pelna.split()
        return cls(imie, nazwisko)


osoba1 = Osoba("Jan", "Kowalski")
# Jan Kowalski
print(osoba1.imie, osoba1.nazwisko)  # Jan Kowalski
# imie, nazwisko = "Jan Kowalski".split()

osoba2 = Osoba.z_nazwy_pelne("Anna Nowak")
print(osoba2.imie, osoba2.nazwisko)  # Anna Nowak
