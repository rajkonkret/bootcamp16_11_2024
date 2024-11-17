# krotka (tupla) - kolekcja niemutowalna
# lepsze wykorzystanie pamięcią
# jedoelementowa krotka, zmienna, niezmienna - stała

tupla1 = "Radek"
print(type(tupla1))  # <class 'str'>

tupla2 = ("Radek")
print(type(tupla2))  # <class 'str'>

tupla3 = "radek",
print(tupla3)  # ('radek',)

# PEP8 sugeruje, by tuplę jednoelementową tworzyć z nawiasami
tupla4 = ("radek",)
print(type(tupla4))  # <class 'tuple'>

tupla_names = "Radek", "Tomek", "Zenek", "Bartek"
print(type(tupla_names))  # <class 'tuple'>
print(tupla_names)  # ('Radek', 'Tomek', 'Zenek', 'Bartek')

temp = 36, 6  # <class 'tuple'>
print(type(temp))  # <class 'tuple'>
print(temp)  # (36, 6)

tupla_liczby = 43, 55, 22.34, 11, 200
tupla_liczby = (43, 55, 22.34, 11, 200)
print(type(tupla_liczby))  # <class 'tuple'>
print(tupla_liczby)  # (43, 55, 22.34, 11, 200)
# ctrl + ] - przejscie na koniec linii

# tupla jest niemutowalna (imutable) - ni emożna zmienić niz w niej
# temp[0] = 1  # TypeError: 'tuple' object does not support item assignment

# del - usnięcie  z pamięci
# w tupli nie da się usunąć pojedynczego jej elementu
# del temp[0] # TypeError: 'tuple' object doesn't support item deletion

# można usunąc całą tuplę (krotkę)
del temp
# print(temp)  # NameError: name 'temp' is not defined

print(tupla_liczby)
# spróbujcie czy na tupli działa slicowanie
print(tupla_liczby[:3])  # (43, 55, 22.34)
print(tupla_liczby[0:3])  # (43, 55, 22.34)
print(tupla_liczby[1:3])  # (55, 22.34)
print(tupla_liczby[2:])  # (22.34, 11, 200)

print(tupla_liczby[-1])
print(tupla_liczby[::-1])  # (200, 11, 22.34, 55, 43)
print(tupla_liczby[-1::-1])  # (200, 11, 22.34, 55, 43)
# [start:stop:krok] krok -1 oznacza krok do tyłu
print(tupla_liczby[1:4:2])  # (55, 11)
# [-1::-1] -> start=-1, stop=0, krok=-1
print(tupla_liczby[:])  # [-1::-1]

print(tupla_names)
print("Radek" in tupla_names)  # True

# count() - zlicza ile razy element występuje w krotce
print(tupla_names.count('Tomek'))  # "Tomek" występuje 1 raz

# index() - sprawdzenie na którym indeksie znajduje się dany element
print(tupla_names.index("Radek"))  # indeks numer 0

# sorted() - sortowanie kolekcji
# sortowanie tupli zwraca nową listę posortowaną
print(sorted(tupla_names))  # ['Bartek', 'Radek', 'Tomek', 'Zenek']

# sortowanie z odwróceniem
print(sorted(tupla_names, reverse=True))  # ['Zenek', 'Tomek', 'Radek', 'Bartek']

print(tupla_names)  # ('Radek', 'Tomek', 'Zenek', 'Bartek')

# rozpakowanie krotki
a, b = 1, 2  # przypisze do zmiennych wartości wg kolejności
print(f"{a=} {b=}")  # a=1 b=2
print(type((1, 2)))  # <class 'tuple'>
# a, b = 1, 2, 3 # ValueError: too many values to unpack (expected 2)
a, *b = 1, 2, 3  # * worek na pozostałe dane
print(f"{a=} {b=}")  # a=1 b=[2, 3]

# ('Radek', 'Tomek', 'Zenek', 'Bartek')
# name1, name2, name3
# * moze byc tylko w jednym miejscu
*name1, name2, name3 = tupla_names
print(f"{name1=} {name2=} {name3=}")
# name1=['Radek', 'Tomek'] name2='Zenek' name3='Bartek'

name1, *name2, name3 = tupla_names
print(f"{name1=} {name2=} {name3=}")
# name1='Radek' name2=['Tomek', 'Zenek'] name3='Bartek'

name1, name2, *name3 = tupla_names
print(f"{name1=} {name2=} {name3=}")
# name1='Radek' name2='Tomek' name3=['Zenek', 'Bartek']

tupla_zadanie = "OLA", 'Ania', "Ada", "Gabi", "Kasia", "Paulina"
i1, i2, *i3, i4 = tupla_zadanie
print(i1, i2, i3, i4)  # OLA Ania ['Ada', 'Gabi', 'Kasia'] Paulina
"""
    Prints the values to a stream, or to sys.stdout by default.

      sep
        string inserted between values, default a space.
      end
        string appended after the last value, default a newline.
      file
        a file-like object (stream); defaults to the current sys.stdout.
      flush
        whether to forcibly flush the stream.
    """
print("Jeden", "Dwa", "Trzy")  # Jeden Dwa Trzy
print("Jeden", "Dwa", "Trzy", sep="")  # "" - pusty separator, JedenDwaTrzy
print("Jeden", "Dwa", "Trzy", sep="=>")  # "" - pusty separator, Jeden=>Dwa=>Trzy
print("Jeden", "Dwa", "Trzy", sep=":")  # "" - Jeden:Dwa:Trzy
print("Jeden", "Dwa", "Trzy", sep=":", end="")  # "" - pusty znak konca linii, Jeden:Dwa:Trzy
print("Dalszy tekst")  # Jeden:Dwa:TrzyDalszy tekst wypisany bez zmiany do nowej linii
print("Radek")  # Radek, w nowej linii bo poprzednia linia ustawiła na domyślny "\n"
# sep: znak oddzielający elelementy (domyślnie " ")
# end: znak na końcu linii (domyślnie "\n" - nowa linia)

lista = list(tupla_names)
print(lista)  # ['Radek', 'Tomek', 'Zenek', 'Bartek']
print(type(lista))  # <class 'list'>
print(len(lista))  # długość 4
