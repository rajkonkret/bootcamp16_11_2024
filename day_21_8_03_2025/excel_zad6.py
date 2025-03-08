import pandas as pd

df = pd.read_excel("tabela_przestawna2.xlsx", skiprows=3)

print(df.head())
