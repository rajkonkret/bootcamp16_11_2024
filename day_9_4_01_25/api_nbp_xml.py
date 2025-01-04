import xml.etree.ElementTree as ET
from typing import List

import requests
from pydantic import BaseModel

#     <Rate>
#                 <Currency>rand (Republika Południowej Afryki)</Currency>
#                 <Code>ZAR</Code>
#                 <Mid>0.2210</Mid>
#             </Rate>

url = "https://api.nbp.pl/api/exchangerates/tables/A/?format=xml"

response = requests.get(url)
print(response)
print(response.text)

xml_data = response.content

root = ET.fromstring(xml_data)
print(root)  # <Element 'ArrayOfExchangeRatesTable' at 0x00000203C131FE70>

table_name = root.find(".//Table").text
print(f"Tabela: {table_name}")  # A

date = root.find(".//EffectiveDate").text
print(f"Data tabeli: {date}")  # Data tabeli: 2025-01-03

no = root.find(".//No").text
print(f"Numer tabeli: {no}")  # Numer tabeli: 002/A/NBP/2025

rates = root.findall(".//Rate")
print(rates)

for rate in rates:
    currency = rate.find("Currency").text
    code = rate.find("Code").text
    mid = rate.find("Mid").text
    print(f"{code} : {currency} - {mid}")


# THB : bat (Tajlandia) - 0.1205
# USD : dolar amerykański - 4.1512
# AUD : dolar australijski - 2.5794
# HKD : dolar Hongkongu - 0.5337
# CAD : dolar kanadyjski - 2.8849
# NZD : dolar nowozelandzki - 2.3252
# SGD : dolar singapurski - 3.0299
# EUR : euro - 4.2718
# HUF : forint (Węgry) - 0.010299
# CHF : frank szwajcarski - 4.5658
# GBP : funt szterling - 5.1498
# UAH : hrywna (Ukraina) - 0.0986
# JPY : jen (Japonia) - 0.026398
# CZK : korona czeska - 0.1697
# DKK : korona duńska - 0.5727
# ISK : korona islandzka - 0.029769
# NOK : korona norweska - 0.3644
# SEK : korona szwedzka - 0.3726
# RON : lej rumuński - 0.8588
# BGN : lew (Bułgaria) - 2.1841
# TRY : lira turecka - 0.1173
# ILS : nowy izraelski szekel - 1.1365
# CLP : peso chilijskie - 0.004129
# PHP : peso filipińskie - 0.0714
# MXN : peso meksykańskie - 0.2023
# ZAR : rand (Republika Południowej Afryki) - 0.2210
# BRL : real (Brazylia) - 0.6747
# MYR : ringgit (Malezja) - 0.9225
# IDR : rupia indonezyjska - 0.00025641
# INR : rupia indyjska - 0.048407
# KRW : won południowokoreański - 0.002823
# CNY : yuan renminbi (Chiny) - 0.5672
# XDR : SDR (MFW) - 5.3801

class CurrencyRate(BaseModel):
    currency: str
    code: str
    mid: float


class ExchangeRateTable(BaseModel):
    table: str
    date: str
    number: str
    rates: List[CurrencyRate]


# deserializacja z użyciem Pydantic
currecy_rates = []
for rate in rates:
    currency = rate.find("Currency").text
    code = rate.find("Code").text
    mid = rate.find("Mid").text
    currecy_rates.append(CurrencyRate(currency=currency, code=code, mid=float(mid)))

exchange_rate_table = ExchangeRateTable(
    table=table_name,
    date=date,
    number=no,
    rates=currecy_rates
)

print(exchange_rate_table)
rates_pydantic = exchange_rate_table.rates
for rate in rates_pydantic:
    print(rate)
# currency='ringgit (Malezja)' code='MYR' mid=0.9225
# currency='rupia indonezyjska' code='IDR' mid=0.00025641
