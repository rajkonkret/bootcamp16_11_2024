import pandas as pd

df = pd.read_csv('data.csv')
print(df.info())

# df = df ze zmianami -> inplace
df.fillna(130, inplace=True)
print(df.info())
# RangeIndex: 169 entries, 0 to 168
# Data columns (total 4 columns):
#  #   Column    Non-Null Count  Dtype
# ---  ------    --------------  -----
#  0   Duration  169 non-null    int64
#  1   Pulse     169 non-null    int64
#  2   Maxpulse  169 non-null    int64
#  3   Calories  169 non-null    float64
# dtypes: float64(1), int64(3)
# memory usage: 5.4 KB
# None
print(df.loc[141])
# Duration     60.0
# Pulse        97.0
# Maxpulse    127.0
# Calories    130.0
# Name: 141, dtype: float64

print("Pandas 3.0")
# dla Pandas 3.0
df = pd.read_csv('data.csv')
df.fillna({"Calories": 130}, inplace=True)
df.info()
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 169 entries, 0 to 168
# Data columns (total 4 columns):
#  #   Column    Non-Null Count  Dtype
# ---  ------    --------------  -----
#  0   Duration  169 non-null    int64
#  1   Pulse     169 non-null    int64
#  2   Maxpulse  169 non-null    int64
#  3   Calories  169 non-null    float64
# dtypes: float64(1), int64(3)
# memory usage: 5.4 KB
print(df.loc[141])
# Duration     60.0
# Pulse        97.0
# Maxpulse    127.0
# Calories    130.0
# Name: 141, dtype: float64

print("Pandas 3.0 bezpieczna metoda")
df = pd.read_csv('data.csv')
df['Calories'] = df['Calories'].fillna(130)
df.info()
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 169 entries, 0 to 168
# Data columns (total 4 columns):
#  #   Column    Non-Null Count  Dtype
# ---  ------    --------------  -----
#  0   Duration  169 non-null    int64
#  1   Pulse     169 non-null    int64
#  2   Maxpulse  169 non-null    int64
#  3   Calories  169 non-null    float64
# dtypes: float64(1), int64(3)
# memory usage: 5.4 KB


# -------
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 169 entries, 0 to 168
# Data columns (total 4 columns):
#  #   Column    Non-Null Count  Dtype
# ---  ------    --------------  -----
#  0   Duration  169 non-null    int64
#  1   Pulse     169 non-null    int64
#  2   Maxpulse  169 non-null    int64
#  3   Calories  164 non-null    float64
# dtypes: float64(1), int64(3)
# memory usage: 5.4 KB

df['Calories'].fillna(130, inplace=True)
df.info()
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 169 entries, 0 to 168
# Data columns (total 4 columns):
#  #   Column    Non-Null Count  Dtype
# ---  ------    --------------  -----
#  0   Duration  169 non-null    int64
#  1   Pulse     169 non-null    int64
#  2   Maxpulse  169 non-null    int64
#  3   Calories  169 non-null    float64
# dtypes: float64(1), int64(3)
# memory usage: 5.4 KB

# mean() - średnia arytmetyczna
df = pd.read_csv('data.csv')

x = df['Calories'].mean()
print("Srednia wynosi:", x)  # Srednia wynosi: 375.79999999999995

# zamiana nan na wartości średnie
df['Calories'] = df['Calories'].fillna(x)
print(df.loc[141])
# Srednia wynosi: 375.79999999999995
# Duration     60.0
# Pulse        97.0
# Maxpulse    127.0
# Calories    375.8
# Name: 141, dtype: float64

# median() - mediana, wartość środkowa
data = {"Wiek": [25, 30, 35, 40, 45, 50, 55, 60, 65]}

df = pd.DataFrame(data)
mediana_wiek = df["Wiek"].median()
print("Mediana wieku:", mediana_wiek)  # Mediana wieku: 45.0

df = pd.read_csv("data.csv")

median_data = df["Calories"].median()
print("Mediana:", median_data)
df['Calories'] = df['Calories'].fillna(median_data)
print(df.loc[141])  # Mediana: 318.6
# Duration     60.0
# Pulse        97.0
# Maxpulse    127.0
# Calories    318.6
# Name: 141, dtype: float64

# mode - wartość najczęściej występująca
df = pd.read_csv('data.csv')
mode_data = df['Calories'].mode()  # Najczęściej występująca: 0    300.0
print('Najczęściej występująca:', mode_data)
df['Calories'] = df['Calories'].fillna(mode_data[0])
print(df.loc[141])
# Duration     60.0
# Pulse        97.0
# Maxpulse    127.0
# Calories    300.0
# Name: 141, dtype: float64

# wyswietlenie wierszy posiadajace NaN
df = pd.read_csv('data.csv')
print(df[df.isna().any(axis=1)])
#      Duration  Pulse  Maxpulse  Calories
# 17         45     90       112       NaN
# 27         60    103       132       NaN
# 91         45    107       137       NaN
# 118        60    105       125       NaN
# 141        60     97       127       NaN

# w poszczegolnej kolumnie
print(df[df['Calories'].isna()])
#      Duration  Pulse  Maxpulse  Calories
# 17         45     90       112       NaN
# 27         60    103       132       NaN
# 91         45    107       137       NaN
# 118        60    105       125       NaN
# 141        60     97       127       NaN