# REST API - sposób komunikowania się i wymiany danych pomiędzy klientem i serwerem
# klient np.: przeglądarka
# serwer - tzw backend, serwer, który ma wystawione metody potrafiące obsłużyć żądania klienta
# GET, POST, PUT/PATCH, DELETE - metody http
# GET - pobiera dane
# POST - do tworzenia obiektu, wysyła dane na serwer, w body można przesłać jsona
# PUT/PATCH - aktualizuje obiekt
# DELETE - usunięcie obiektu
# Działanie 	    Instrukcja SQL	HTTP	             DDS
# Create	            INSERT  	PUT / POST	        write
# Read (Retrieve)	    SELECT	    GET	read /          take
# Update	            UPDATE	    POST / PUT / PATCH	write
# Delete (Destroy)	    DELETE	    DELETE	            dispose
from typing import List

import requests  # biblioteka do obsługi metod http
from pydantic import BaseModel

# pip install requests

url = "http://api.open-notify.org/astros.json"
response = requests.get(url)
print(response)  # <Response [200]>

# statusy http
# https://pl.wikipedia.org/wiki/Kod_odpowiedzi_HTTP
# 2xx - OK
# 3xx - warningi, przekierowania
# 4xx - 404 - brak zasobu, 400 Bad Request błedy parametrów, błedy po stronie klienta
# 5xx - błędy serwera, 500 internal Server Error

# czysty json
print(response.text)

# zamiana jsona na słownik
response_data = response.json()
print(type(response_data))  # <class 'dict'>

# wypisac wszystkie klucze ze słownika
for k in response_data:
    print(k)
# people
# number
# message

for k, v in response_data.items():
    print(k, "=>", v)

# people => [{'craft': 'ISS', 'name': 'Oleg Kononenko'},
#            {'craft': 'ISS', 'name': 'Nikolai Chub'},
#            {'craft': 'ISS', 'name': 'Tracy Caldwell Dyson'},
#            {'craft': 'ISS', 'name': 'Matthew Dominick'},
#            {'craft': 'ISS', 'name': 'Michael Barratt'},
#            {'craft': 'ISS', 'name': 'Jeanette Epps'},
#            {'craft': 'ISS', 'name': 'Alexander Grebenkin'},
#            {'craft': 'ISS', 'name': 'Butch Wilmore'},
#            {'craft': 'ISS', 'name': 'Sunita Williams'},
#            {'craft': 'Tiangong', 'name': 'Li Guangsu'},
#            {'craft': 'Tiangong', 'name': 'Li Cong'},
#            {'craft': 'Tiangong', 'name': 'Ye Guangfu'}]
# number => 12
# message => success

people_list = response_data['people']
for i in people_list:
    print(i)
# {'craft': 'ISS', 'name': 'Oleg Kononenko'}
# {'craft': 'ISS', 'name': 'Nikolai Chub'}
# {'craft': 'ISS', 'name': 'Tracy Caldwell Dyson'}
# {'craft': 'ISS', 'name': 'Matthew Dominick'}
# {'craft': 'ISS', 'name': 'Michael Barratt'}
# {'craft': 'ISS', 'name': 'Jeanette Epps'}
# {'craft': 'ISS', 'name': 'Alexander Grebenkin'}
# {'craft': 'ISS', 'name': 'Butch Wilmore'}
# {'craft': 'ISS', 'name': 'Sunita Williams'}
# {'craft': 'Tiangong', 'name': 'Li Guangsu'}
# {'craft': 'Tiangong', 'name': 'Li Cong'}
# {'craft': 'Tiangong', 'name': 'Ye Guangfu'}

# wyswietlic name dla matthew
matthew = response_data['people'][3]['name']
print(matthew)  # Matthew Dominick


class Astronaut(BaseModel):
    craft: str
    name: str


class AstroData(BaseModel):
    message: str
    number: int
    people: List[Astronaut]


data = AstroData(**response_data)
print(data)
# message = 'success'
# number = 12
# people = [Astronaut(craft='ISS', name='Oleg Kononenko'), Astronaut(craft='ISS', name='Nikolai Chub'),
#           Astronaut(craft='ISS', name='Tracy Caldwell Dyson'), Astronaut(craft='ISS', name='Matthew Dominick'),
#           Astronaut(craft='ISS', name='Michael Barratt'), Astronaut(craft='ISS', name='Jeanette Epps'),
#           Astronaut(craft='ISS', name='Alexander Grebenkin'), Astronaut(craft='ISS', name='Butch Wilmore'),
#           Astronaut(craft='ISS', name='Sunita Williams'), Astronaut(craft='Tiangong', name='Li Guangsu'),
#           Astronaut(craft='Tiangong', name='Li Cong'), Astronaut(craft='Tiangong', name='Ye Guangfu')]
print(data.message)  # success
print(data.number)  # 12

for people in data.people:
    print(people)
    print(people.name)
# craft='ISS' name='Oleg Kononenko'
# Oleg Kononenko
# craft='ISS' name='Nikolai Chub'
# Nikolai Chub
# craft='ISS' name='Tracy Caldwell Dyson'
# Tracy Caldwell Dyson
# craft='ISS' name='Matthew Dominick'
# Matthew Dominick
# craft='ISS' name='Michael Barratt'
# Michael Barratt
# craft='ISS' name='Jeanette Epps'
# Jeanette Epps
# craft='ISS' name='Alexander Grebenkin'
# Alexander Grebenkin
# craft='ISS' name='Butch Wilmore'
# Butch Wilmore
# craft='ISS' name='Sunita Williams'
# Sunita Williams
# craft='Tiangong' name='Li Guangsu'
# Li Guangsu
# craft='Tiangong' name='Li Cong'
# Li Cong
# craft='Tiangong' name='Ye Guangfu'
# Ye Guangfu

for p in data.people:
    print(p.__class__.__name__)  # Astronaut
