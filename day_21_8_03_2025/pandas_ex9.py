import pandas as pd

df = pd.read_csv('data_with_date.csv')
print(df.to_string())

# informacja o duplikatach True - wiersz zduplikowany
print(df.duplicated())

# usunięcie duplikatów
df.drop_duplicates(inplace=True)
print(df.to_string())
