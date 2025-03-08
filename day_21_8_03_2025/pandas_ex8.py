import pandas as pd
from pandas.core.interchange.dataframe_protocol import DataFrame

data = pd.read_csv('data_with_date.csv')

print(data)
data.loc[7, "Duration"] = 45
print(data.loc[7])
# Duration              45
# Date        '2020/12/08'
# Pulse                104
# Maxpulse             134
# Calories           253.3
# Name: 7, dtype: object

data = pd.read_csv('data_with_date.csv')

for x in data.index:
    if data.loc[x, "Duration"] > 120:
        data.loc[x, "Duration"] = 120

print(data)

data = pd.read_csv('data_with_date.csv')
for x in data.index:
    if data.loc[x, "Duration"] > 120:
        data.drop(x, inplace=True)

print(data)

df = pd.DataFrame({'Miasto': ['Warszawa', 'Kraków', "Łódź", "Warszawa", "Gliwice"]})
print(df)

# df['Miasto'].replace('Warszawa', 'Warszawa - Stolica', inplace=True)  # stare podejscie
df['Miasto'] = df['Miasto'].replace('Warszawa', 'Warszawa - Stolica')  # bezpieczne podejście

print(df.to_string())

df = pd.DataFrame({'Miasto': ['Warszawa', 'Kraków', "Łódź", "Warszawa", "Gliwice"]})
df['Miasto'] = df['Miasto'].replace({'Warszawa': 'Warszawa - Stolica', "Kraków": "Kraków - Zamkowy"})
print(df)
# 0  Warszawa - Stolica
# 1    Kraków - Zamkowy
# 2                Łódź
# 3  Warszawa - Stolica
# 4             Gliwice

df = pd.DataFrame({"Wiek": [18, 25, 30, 15, 40]})
print(df)
df['Kategoria'] = "Dorosły"
df.loc[df['Wiek'] < 18, "Kategoria"] = 'Niepołnoletni'
print(df)
#    Wiek      Kategoria
# 0    18        Dorosły
# 1    25        Dorosły
# 2    30        Dorosły
# 3    15  Niepołnoletni
# 4    40        Dorosły

df = pd.DataFrame({'Miasto': ['Warszawa', 'Kraków', "Łódź", "Warszawa", "Gliwice"]})
df['Miasto'] = df['Miasto'].replace(r'Łódź', "Łódź Przemysłowa", regex=True)
print(df.to_string())
# 0          Warszawa
# 1            Kraków
# 2  Łódź Przemysłowa
# 3          Warszawa
# 4           Gliwice

df = pd.DataFrame({"Wiek": [18, 25, 30, 15, 40]})
df['Kategoria'] = df['Wiek'].apply(lambda x: 'Senior' if x > 60 else 'Dorosły')
print(df)
#    Wiek Kategoria
# 0    18   Dorosły
# 1    25   Dorosły
# 2    30   Dorosły
# 3    15   Dorosły
# 4    40   Dorosły

df = pd.DataFrame({"Wiek": [18, 25, 30, 15, 40, 65]})


def zmien(x):
    if x > 60:
        return "Senior"
    else:
        return "Dorosły"


df['Kategoria'] = df['Wiek'].apply(zmien)
print(df)
#    Wiek Kategoria
# 0    18   Dorosły
# 1    25   Dorosły
# 2    30   Dorosły
# 3    15   Dorosły
# 4    40   Dorosły
# 5    65    Senior
