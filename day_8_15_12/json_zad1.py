# json typ danych para klucz wartość
# {"name":"John", "age":30, "car":null}
# podwójne cudzysłowia obowiązkowe
# None -> null
# wykorzystywany w plikach konfiguracyjnych
# i do komunikacji internetowej między sytemami
import json

person_dict = {'name': 'Radek', 'age': 40, 'czy_pali': None}
print(type(person_dict))  # <class 'dict'>

with open('nasze_dane.json', 'w') as f:
    json.dump(person_dict, f)
    # {"name": "Radek", "age": 40, "czy_pali": null}

# beautify
with open('nasze_dane_b.json', "w") as file:
    json.dump(person_dict, file, indent=4)
# {
#     "name": "Radek",
#     "age": 40,
#     "czy_pali": null
# }

# posortowane klucze alfabetycznie
with open('nasze_dane_sort.json', "w") as file:
    json.dump(person_dict, file, indent=4, sort_keys=True)
# {
#     "age": 40,
#     "czy_pali": null,
#     "name": "Radek"
# }

with open("nasze_dane.json", "r") as f:
    data = json.load(f)

print(data)
# {'name': 'Radek', 'age': 40, 'czy_pali': None}
print(type(data))  # <class 'dict'>
print(data['name'])  # Radek

# zamiana słowik na jsona - odpowiadjący mu str
json_text = json.dumps(data)
print(json_text)  # {"name": "Radek", "age": 40, "czy_pali": null}
print(type(json_text))  # <class 'str'>

dict_json = json.loads(json_text)
print(dict_json)  # {'name': 'Radek', 'age': 40, 'czy_pali': None}
print(type(dict_json))  # <class 'dict'>
print(dict_json['name'])  # Radek
