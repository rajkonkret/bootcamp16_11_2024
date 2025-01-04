# zapytanie o pojedynczą walute
# wypis nazwe i sredni kurs dnia
# słownikiem
# obiektami

# https://api.nbp.pl/api/exchangerates/rates/{table}/{code}/
# Table – typ tabeli
# No – numer tabeli
# TradingDate – data notowania (dotyczy tabeli C)
# EffectiveDate – data publikacji
# Rates – lista kursów poszczególnych walut w tabeli
# Country – nazwa kraju
# Symbol – symbol waluty (numeryczny, dotyczy kursów archiwalnych)
# Currency – nazwa waluty
# Code – kod waluty
# Bid – przeliczony kurs kupna waluty (dotyczy tabeli C)
# Ask – przeliczony kurs sprzedaży waluty (dotyczy tabeli C)
# Mid – przeliczony kurs średni waluty (dotyczy tabel A oraz B)
# {table} – typ tabeli (A, B, lub C)
# {code} – trzyliterowy kod waluty (standard ISO 4217)
# {topCount} – liczba określająca maksymalną liczność zwracanej serii danych
# {date}, {startDate}, {endDate} – data w formacie RRRR-MM-DD (standard ISO 8601)
import requests

url = "https://api.nbp.pl/api/exchangerates/rates/A/USD/"
response = requests.get(url)
print(response)
print(response.text)

table = response.json()
print(table)
print(type(table))  # <class 'dict'>
# {'table': 'A', 'currency': 'dolar amerykański', 'code': 'USD',
# 'rates': [{'no': '002/A/NBP/2025', 'effectiveDate': '2025-01-03', 'mid': 4.1512}]}
print(f"Waluta: {table['currency']}")  # Waluta: dolar amerykański
print(f"Rates: {table['rates']}")
# Rates: [{'no': '002/A/NBP/2025', 'effectiveDate': '2025-01-03', 'mid': 4.1512}]
print(f"Kurs {table['currency']} wynosi {table['rates'][0]['mid']} pln")  # Kurs dolar amerykański wynosi 4.1512 pln
