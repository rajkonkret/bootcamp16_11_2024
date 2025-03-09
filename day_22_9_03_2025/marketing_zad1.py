import pandas as pd

# df = pd.read_csv('marketing_r.csv')
df = pd.read_csv("marketing_r.csv", sep=",")
print(df.head(1).to_string())
print(df.describe())
df.info()  # nie potrzebuje printa

# "converted" jaki ma typ?
print(df['converted'].dtype)  # object

# zamienic kolumne na typ danych bool
df['converted'] = df['converted'].astype('bool')
print(df['converted'].dtype) # bool
df.info()
print(df.head(1).to_string())