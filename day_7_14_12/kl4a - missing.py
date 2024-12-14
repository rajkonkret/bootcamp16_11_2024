# __missing__ - metoda wykonywana gdy nie ma klucza w słowniku

class DefaultDict(dict):
    def __missing__(self, key):
        return "default"


d_python = {}
print(type(d_python))  # <class 'dict'>
print(d_python)  # {}
# print(d_python['name']) # KeyError: 'name'
d_python['name'] = "Radek"
print(d_python['name'])  # Radek

d1 = DefaultDict()
print(d1['name'])  # default - nadpisaliśmy metodę __missing__


# Zrobić słownik,
# który, gdy  nie ma klucza w słowniku,
# dopisze ten klucz  z wartością domyślną
class AutoDict(dict):
    def __missing__(self, key):
        self[key] = 0
        return key


d2 = AutoDict()
print(d2)  # {}
print(d2['name'])  # name
print(d2)  # {'name': 0}
print(d2['name'])  # 0
d2['name'] = "Radek"
print(d2['name'])  # Radek


# słownik, gdzie klucze są zapamiętane mała literą
# zwrócimy wartośc dla klucza niezależnie od wielkości liter
# print(1.lower())# SyntaxError: invalid decimal literal
# print(2.casefold())  # SyntaxError: invalid decimal literal
class CaseInsensitiveDict(dict):
    def __missing__(self, key):
        if isinstance(key, str):  # sprawdza czy key jest typu str
            return self.get(key.casefold())


d3 = CaseInsensitiveDict()
d3['name'] = "Radek"
print(d3["NaMe"])  # Radek
d3[1] = "Tomek"
print(d3)  # {'name': 'Radek', 1: 'Tomek'}
print(d3[1])  # Tomek
