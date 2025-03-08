import pandas as pd

df = pd.read_excel("dane.xlsx")

df.info()
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 5 entries, 0 to 4
# Data columns (total 7 columns):
#  #   Column    Non-Null Count  Dtype
# ---  ------    --------------  -----
#  0   Imię      5 non-null      object
#  1   Wiek      4 non-null      float64
#  2   Miasto    5 non-null      object
#  3   Sprzedaż  5 non-null      int64
#  4   Telefon   5 non-null      object
#  5   Data      5 non-null      datetime64[ns]
#  6   Produkt   5 non-null      object
# dtypes: datetime64[ns](1), float64(1), int64(1), object(4)
# memory usage: 412.0+ bytes
print(df.isna().sum())
# Imię        0
# Wiek        1
# Miasto      0
# Sprzedaż    0
# Telefon     0
# Data        0
# Produkt     0
# dtype: int64

# uzupełnic brakujące dane śrdnią
# df['Calories'] = df['Calories'].fillna(median_data)
df["Wiek"] = df['Wiek'].fillna(df['Wiek'].mean())
print(df.isna().sum())
print(df)
# mię        0
# Wiek        0
# Miasto      0
# Sprzedaż    0
# Telefon     0
# Data        0
# Produkt     0
# dtype: int64
#     Imię  Wiek    Miasto  Sprzedaż         Telefon       Data     Produkt
# 0   Anna  25.0  Warszawa      5000       123456789 2024-01-15      Laptop
# 1    Jan  30.0    Kraków      7000  48-123-456-789 2023-12-10      Tablet
# 2  Maria  35.0      Łódź      6000     123 456 789 2024-02-20  Smartphone
# 3  Piotr  40.0    Gdańsk      8000   (123) 456-789 2023-11-05     Monitor
# 4  Kasia  32.5    Poznań      7500       987654321 2024-03-01    Drukarka

df = pd.read_excel("dane.xlsx")
print(df.isna().sum())

df.dropna(inplace=True)
print(df.isna().sum())
# Imię        0
# Wiek        1
# Miasto      0
# Sprzedaż    0
# Telefon     0
# Data        0
# Produkt     0
# dtype: int64
# Imię        0
# Wiek        0
# Miasto      0
# Sprzedaż    0
# Telefon     0
# Data        0
# Produkt     0
# dtype: int64

df = pd.read_excel("dane.xlsx")
print("Ilość duplikatów:", df.duplicated().sum())  # Ilość duplikatów: 0

duplicate_row = df.iloc[1:2]
print(duplicate_row)

df = pd.concat([df, duplicate_row], ignore_index=True)
print(df)

print("Ilość duplikatów:", df.duplicated().sum())  # Ilość duplikatów: 1
df.drop_duplicates(inplace=True)
print(df)
print("Ilość duplikatów:", df.duplicated().sum())
#     Imię  Wiek    Miasto  Sprzedaż         Telefon       Data     Produkt
# 0   Anna  25.0  Warszawa      5000       123456789 2024-01-15      Laptop
# 1    Jan  30.0    Kraków      7000  48-123-456-789 2023-12-10      Tablet
# 2  Maria  35.0      Łódź      6000     123 456 789 2024-02-20  Smartphone
# 3  Piotr  40.0    Gdańsk      8000   (123) 456-789 2023-11-05     Monitor
# 4  Kasia   NaN    Poznań      7500       987654321 2024-03-01    Drukarka
# Ilość duplikatów: 0

df_filtr = df[df["Wiek"] > 30]
print(df_filtr)
#     Imię  Wiek  Miasto  Sprzedaż        Telefon       Data     Produkt
# 2  Maria  35.0    Łódź      6000    123 456 789 2024-02-20  Smartphone
# 3  Piotr  40.0  Gdańsk      8000  (123) 456-789 2023-11-05     Monitor

df_filtr = df[(df["Wiek"] > 30) & (df["Miasto"] == "Warszawa")]
print(df_filtr)
# Empty DataFrame
# Columns: [Imię, Wiek, Miasto, Sprzedaż, Telefon, Data, Produkt]
# Index: []

print(df)
# df["Miasto"].replace("Kraków", "KrK", inplace=True) stare podejście
df["Miasto"] = df["Miasto"].replace("Kraków", "KrK")
print(df)
#     Imię  Wiek    Miasto  Sprzedaż         Telefon       Data     Produkt
# 0   Anna  25.0  Warszawa      5000       123456789 2024-01-15      Laptop
# 1    Jan  30.0       KrK      7000  48-123-456-789 2023-12-10      Tablet
# 2  Maria  35.0      Łódź      6000     123 456 789 2024-02-20  Smartphone
# 3  Piotr  40.0    Gdańsk      8000   (123) 456-789 2023-11-05     Monitor
# 4  Kasia   NaN    Poznań      7500       987654321 2024-03-01    Drukarka

df.loc[df["Wiek"] < 18, "Status"] = "Niepełnoletni"
print(df)

# sortowanie danych
df.sort_values(by="Wiek", ascending=False, inplace=True)
print(df)
