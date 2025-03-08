import pandas as pd

df = pd.read_excel("dane.xlsx", sheet_name="Sprzedaż")
print(df)

mediana = df["Sprzedaż"].median()
print('Mediana:', mediana)  # Mediana: 19500.0
