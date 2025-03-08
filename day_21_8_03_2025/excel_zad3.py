import pandas as pd

df = pd.read_excel("dane.xlsx", sheet_name="Produkty")
print(df)

df["Nowa Cena"] = df["Cena"] * 1.23
print(df)
#       Produkt  Cena  Nowa Cena
# 0      Laptop  4500     5535.0
# 1      Tablet  1200     1476.0
# 2  Smartphone  2800     3444.0
# 3     Monitor  1500     1845.0
# 4    Drukarka   700      861.0

# zamiana nazwy kolumny
df.rename(columns={"Cena": "Koszt"}, inplace=True)
print(df)
#       Produkt  Koszt  Nowa Cena
# 0      Laptop   4500     5535.0
# 1      Tablet   1200     1476.0
# 2  Smartphone   2800     3444.0
# 3     Monitor   1500     1845.0
# 4    Drukarka    700      861.0

df = pd.read_excel("dane.xlsx", sheet_name=None)
print(df)

df = pd.read_excel("dane.xlsx", sheet_name="Dane_Ogolne")
print(df)
#     Imię  Wiek    Miasto  Sprzedaż         Telefon       Data     Produkt
# 0   Anna  25.0  Warszawa      5000       123456789 2024-01-15      Laptop
# 1    Jan  30.0    Kraków      7000  48-123-456-789 2023-12-10      Tablet
# 2  Maria  35.0      Łódź      6000     123 456 789 2024-02-20  Smartphone
# 3  Piotr  40.0    Gdańsk      8000   (123) 456-789 2023-11-05     Monitor
# 4  Kasia   NaN    Poznań      7500       987654321 2024-03-01    Drukarka
df['Data'] = pd.to_datetime(df['Data'])
print(df)

df["Rok"] = df["Data"].dt.year
print(df)
df['Miesiąc'] = df["Data"].dt.month
print(df)
#     Imię  Wiek    Miasto  Sprzedaż  ...       Data     Produkt   Rok  Miesiąc
# 0   Anna  25.0  Warszawa      5000  ... 2024-01-15      Laptop  2024        1
# 1    Jan  30.0    Kraków      7000  ... 2023-12-10      Tablet  2023       12
# 2  Maria  35.0      Łódź      6000  ... 2024-02-20  Smartphone  2024        2
# 3  Piotr  40.0    Gdańsk      8000  ... 2023-11-05     Monitor  2023       11
# 4  Kasia   NaN    Poznań      7500  ... 2024-03-01    Drukarka  2024        3
