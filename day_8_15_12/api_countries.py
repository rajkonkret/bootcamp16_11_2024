from typing import List

import requests
from pydantic import BaseModel

url = "https://restcountries.com/v3.1/name/Poland"

response = requests.get(url)
print(response)

# print(response.text)
data = response.json()  # zamian ana słownik
print(type(data))  # <class 'list'>
# print(data[0])  # wypisanie pierwszego eleemntu z listy
country = data[0]

print(f"Nazwa karaju: {country['name']}")
# Nazwa karaju: {'common': 'Poland', 'official': 'Republic of Poland',
#                'nativeName': {'pol': {'official': 'Rzeczpospolita Polska', 'common': 'Polska'}}}
print(f"Nazwa główna: {country['name']['common']}")  # Nazwa główna: Poland
print(f"Nazwa oficjalna: {country['name']['official']}")  # Nazwa oficjalna: Republic of Poland

# "capital": [
#     "Warsaw"
# ],
print(f"Stolica kraju: {country['capital']}")  # Stolica kraju: ['Warsaw']
print(f"Stolica kraju: {country['capital'][0]}")  # Stolica kraju: Warsaw

#    "population": 37950802,
print(f"Liczba ludności: {country['population']}")  # Liczba ludności: 37950802


class Pol(BaseModel):
    official: str
    common: str


class NativeName(BaseModel):
    pol: Pol


class Name(BaseModel):
    common: str
    # official: int # Input should be a valid integer, unable to parse string as an integer
    official: str  # Input should be a valid integer, unable to parse string as an integer
    nativeName: NativeName  # nativeName=NativeName(pol=Pol(official='Rzeczpospolita Polska', common='Polska'))
    # nativeName: dict, nativeName={'pol': {'official': 'Rzeczpospolita Polska', 'common': 'Polska'}}


class CountryInfo(BaseModel):
    name: Name
    capital: List[str]
    population: int


country_data = [CountryInfo(**data) for data in response.json()]

for country in country_data:
    # print(country)
    # name = Name(common='Poland', official='Republic of Poland',
    #             nativeName=NativeName(pol=Pol(official='Rzeczpospolita Polska', common='Polska')))
    # capital = ['Warsaw']
    # population = 37950802

    print(type(country))  # <class '__main__.CountryInfo'>
    print(
        country.name)  # common='Poland' official='Republic of Poland' nativeName=NativeName(pol=Pol(official='Rzeczpospolita Polska', common='Polska'))
    print(country.name.common)  # Poland
    print(country.name.official)  # Republic of Poland
    print(country.population)  # 37950802
    print(country.capital)  # ['Warsaw']
    print(country.capital[0])  # Warsaw

    print(country.name.nativeName)  # pol=Pol(official='Rzeczpospolita Polska', common='Polska')
    print(country.name.nativeName.pol)  # official='Rzeczpospolita Polska' common='Polska'
    print(type(country.name.nativeName.pol))  # <class '__main__.Pol'>

    print(country.name.nativeName.pol.official)  # Rzeczpospolita Polska
    print(country.name.nativeName.pol.common)  # Polska

    print(type(country.name.nativeName.pol.common))  # <class 'str'>
