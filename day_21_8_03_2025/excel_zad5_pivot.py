import pandas as pd

df = pd.read_excel("tabela_przestawna.xlsx")
print(df)

pivot = pd.pivot_table(df, values="Sprzedaż", index="Region", columns="Produkt", aggfunc="sum", fill_value=0)
print(pivot)
# Produkt   Drukarka  Laptop  Monitor  Smartphone  Tablet
# Region
# Centrum          0       0    13000           0   14000
# Południe         0   18000        0       22000       0
# Północ           0   15000        0           0   12000
# Wschód       10500       0        0       19500       0
# Zachód           0   16000    17500           0       0