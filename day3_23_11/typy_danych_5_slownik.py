# słownik - para klucz - wartosc
# {"klucz": 'wartość'}
# klucze nie mogą się powtarzać
# słownik jest odpowiednikiem jsona w pythona

my_dict = {"A": "one", "B": 'two', 'C': 'three', 'D': 'four'}
print(my_dict)  # {'A': 'one', 'B': 'two', 'C': 'three', 'D': 'four'}
print(type(my_dict))  # <class 'dict'>

empty_dict = dict()  # tworzenie pustego słownika
print(empty_dict)  # {} pusty słownik

empty_dict2 = {}
print(empty_dict2)  # {} pusty słownik
print(type(empty_dict2))  # <class 'dict'>

dict_with_integer = {1: 'one', 2: "two", 3: 'three'}
print(dict_with_integer)  # {1: 'one', 2: 'two', 3: 'three'}

dict_mixed = {1: 'one', 'A': "two", 3: 'three'}
print(dict_mixed)
# ctrl alt l - formatuje zgodnie z PEP8

print(dict_mixed.keys())  # dict_keys([1, 'A', 3]), klucze
print(dict_mixed.values())  # dict_values(['one', 'two', 'three']), wartości
print(dict_mixed.items())  # dict_items([(1, 'one'), ('A', 'two'), (3, 'three')]), pary

print(dict_with_integer.keys())  # dict_keys([1, 2, 3])

dict_with_list = {1: 'one', 2: 'two', "A": ['asif', 'jhon', 'maria']}
print(dict_with_list)  # {1: 'one', 2: 'two', 'A': ['asif', 'jhon', 'maria']}

dict_with_list_and_tuple = {1: 'one', 2: 'two', "A": ['asif', 'jhon', 'maria'], 'B': ('Bat', 'cat', 'hat')}
print(dict_with_list_and_tuple)
# {1: 'one', 2: 'two', 'A': ['asif', 'jhon', 'maria'], 'B': ('Bat', 'cat', 'hat')}

dict_with_all = {1: 'one',
                 2: 'two',
                 'A': ['asif', 'jhon', 'maria'],
                 "B": ('Bat', 'cat', 'hat'),
                 "C": {"Name", 'age', 10}}
print(dict_with_all)
# {1: 'one',
#  2: 'two',
#  'A': ['asif', 'jhon', 'maria'],
#  'B': ('Bat', 'cat', 'hat'),
#  'C': {10, 'Name', 'age'}}

dict_with_dict = {1: 'one',
                  2: 'two',
                  'A': ['asif', 'jhon', 'maria'],
                  "B": ('Bat', 'cat', 'hat'),
                  "C": {"Name", 'age', 10},
                  "D": {"Name": "Radek", "age": 99}}
print(dict_with_dict)
# {1: 'one', 2: 'two', 'A': ['asif', 'jhon', 'maria'], 'B': ('Bat', 'cat', 'hat'), 'C': {'age', 10, 'Name'},
#  'D': {'Name': 'Radek', 'age': 99}}

# tworzenie słownika  z sekwencji kluczy
keys = {'a', 'b', 'c', 'd'}
my_dict2 = dict.fromkeys(keys)
print(my_dict2)  # {'b': None, 'c': None, 'd': None, 'a': None}
# None - nie wiem, nic, stan nieokreślony

value = 10
my_dict3 = dict.fromkeys(keys, value)
print(my_dict3)  # {'d': 10, 'b': 10, 'a': 10, 'c': 10}

value = [10, 20, 30]
my_dict4 = dict.fromkeys(keys, value)
print(my_dict4)
# {'a': [10, 20, 30], 'd': [10, 20, 30], 'b': [10, 20, 30], 'c': [10, 20, 30]}

# zastosowanie fromkeys() do usunięcia duplikatów z listy
# od pythona 3.7 można zalożyc, ze zachowa kolejność gdy mamy listę
keys = [1, 2, 2, 3, 4, 4, 5]  # lista z duplikatami
dict_unique = dict.fromkeys(keys)
print(dict_unique)  # {1: None, 2: None, 3: None, 4: None, 5: None}
list_unique = list(dict_unique)
print(list_unique)  # [1, 2, 3, 4, 5]

print(list(dict.fromkeys(keys)))  # w jednej linijce, [1, 2, 3, 4, 5]

# wypisanie wartości dla kluczy
print(my_dict["A"])  # one
# powypisywac ze słowników wybrane klucze
print(dict_with_integer[1])  # one
print(dict_with_all['C'])  # {'age', 10, 'Name'}

# print(my_dict4['e'])  # KeyError: 'e'

print(my_dict4.get("a"))  # [10, 20, 30]
print(my_dict4.get("e"))  # None
# możemy ustawić wartość domyślną jaka będzie zwracana gdy nie ma klucza w słowniku
print(my_dict4.get("e", "Nie ma"))  # Nie ma

my_dict5 = {'Name': "Radek", "ID": 12345, "DDB": 1991, 'Address': "Warsaw"}
print(my_dict5)  # {'Name': 'Radek', 'ID': 12345, 'DDB': 1991, 'Address': 'Warsaw'}

print(my_dict5['DDB'])  # 1991

# nadpisanie wartości dla klucza
my_dict5['DDB'] = '1980'
print(my_dict5)  # {'Name': 'Radek', 'ID': 12345, 'DDB': '1980', 'Address': 'Warsaw'}
my_dict5['Address'] = "Warsaw Centrum"
print(my_dict5)  # {'Name': 'Radek', 'ID': 12345, 'DDB': '1980', 'Address': 'Warsaw Centrum'}

dict1 = {"DDB": 1995}
print(dict1)  # {'DDB': 1995}
print(type(dict1))  # <class 'dict'>

# update słownika innym słownikiem
my_dict5.update(dict1)
print(my_dict5)
# {'Name': 'Radek', 'ID': 12345, 'DDB': 1995, 'Address': 'Warsaw Centrum'}, podmieniło wartość dla klucza DDB

# dodanie klucza do słownika i wartości
my_dict5['Job'] = "Developer"
print(my_dict5)
# {'Name': 'Radek', 'ID': 12345, 'DDB': 1995, 'Address': 'Warsaw Centrum', 'Job': 'Developer'}

dict2 = {'cpi': 3.41}  # float, zmiennoprzecinkowe
print(dict2)  # {'cpi': 3.41}

# update słownika
# dodanie klucza jesli taki jescze nie istnieje w docelowym słowniku
# docelowy czyli my_dict5
my_dict5.update(dict2)
print(my_dict5)
# {'Name': 'Radek', 'ID': 12345, 'DDB': 1995, 'Address': 'Warsaw Centrum', 'Job': 'Developer', 'cpi': 3.41}
