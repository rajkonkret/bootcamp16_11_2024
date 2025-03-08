import pandas as pd

df = pd.read_excel("dane.xlsx")
print(df)
print(df.head())  # pierwsze 5

df = pd.read_excel("dane.xlsx", usecols=["Imię", "Wiek"])
print(df)
#     Imię  Wiek
# 0   Anna  25.0
# 1    Jan  30.0
# 2  Maria  35.0
# 3  Piotr  40.0
# 4  Kasia   NaN

df = pd.read_excel("dane.xlsx", sheet_name="Produkty")
print(df)
#       Produkt  Cena
# 0      Laptop  4500
# 1      Tablet  1200
# 2  Smartphone  2800
# 3     Monitor  1500
# 4    Drukarka   700

df = pd.read_excel("dane.xlsx", sheet_name=None)
print(list(df.keys()))  # ['Dane_Ogolne', 'Sprzedaż', 'Klienci', 'Produkty']

xlsx = pd.ExcelFile('dane.xlsx')
print(xlsx.sheet_names)  # ['Dane_Ogolne', 'Sprzedaż', 'Klienci', 'Produkty']
xlsx.close()

df = pd.read_excel("dane.xlsx")
df.to_excel("wyniki.xlsx")
df.to_excel("wyniki_not_index.xlsx", index=False)

# dodanie arkusza do excela
with pd.ExcelWriter('wyniki.xlsx', mode="a", engine="openpyxl") as writer:
    df.to_excel(writer, sheet_name="NoweDane")

# zapisanie do róznych arkuszy
df1 = pd.read_excel("dane.xlsx")
df2 = pd.read_excel("dane.xlsx", sheet_name="Produkty")
with pd.ExcelWriter("raport.xlsx", mode="a", engine="openpyxl") as writer:
    df1.to_excel(writer, sheet_name="Sprzedaż")
    df2.to_excel(writer, sheet_name="Klienci")
