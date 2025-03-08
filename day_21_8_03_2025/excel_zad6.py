import pandas as pd
with open("tabela_przestawna3.xlsx", "rb") as f:
    content = f.read()
with open("tabela_przestawna3.xlsx", "rb") as f:
    content = f.read(500)  # Pobieramy pierwsze 500 bajtów

print(content[:200])  # Podgląd pierwszych 200 bajtów

print("Rozmiar pliku:", len(content), "bajtów")
# df = pd.read_excel("tabela_przestawna3.xlsx", skiprows=3, engine="openpyxl")
df = pd.read_excel("fix.xlsx", skiprows=3, engine="openpyxl")

print(df.head())
