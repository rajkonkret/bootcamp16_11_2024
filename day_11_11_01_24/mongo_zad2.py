import datetime

from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

db = client['przykladowa_baza']
kolekcja = db['uzytkownicy']

# kolekcja.insert_one(
#     {'imie': 'Jan', 'nazwisko': "Kowalski", 'wiek': 30}
# )

kolekcja.insert_many(
    [
        {'imie': 'Anna', 'nazwisko': 'Nowak', 'wiek': 25},
        {'imie': 'Paweł', 'nazwisko': 'Wiśniewski', 'wiek': 19, 'czas': datetime.datetime.now().strftime("%d/%m/%Y")},
    ]
)

for uzytkownik in kolekcja.find():
    print(uzytkownik)

print(kolekcja.find_one({"imie": "Jan"}))
# {'_id': ObjectId('67827dd362a66e2a3d492026'), 'imie': 'Jan', 'nazwisko': 'Kowalski', 'wiek': 30}

client.close()
# {'_id': ObjectId('67827dd362a66e2a3d492026'), 'imie': 'Jan', 'nazwisko': 'Kowalski', 'wiek': 30}
# {'_id': ObjectId('67827dd362a66e2a3d492026'), 'imie': 'Jan', 'nazwisko': 'Kowalski', 'wiek': 30}
# {'_id': ObjectId('67827e665a61ecb2c57d54c6'), 'imie': 'Anna', 'nazwisko': 'Nowak', 'wiek': 25}
# {'_id': ObjectId('67827e665a61ecb2c57d54c7'), 'imie': 'Paweł', 'nazwisko': 'Wiśniewski', 'wiek': 19}
