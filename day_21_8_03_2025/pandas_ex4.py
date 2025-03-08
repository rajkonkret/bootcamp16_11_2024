import pandas as pd

df = pd.read_csv('data.csv')

# wyswietlenie pierwszych 10
print(df.head(10))

# wyświetlenie pierwszych 5
print(df.head())
#    Duration  Pulse  Maxpulse  Calories
# 0        60    110       130     409.1
# 1        60    117       145     479.0
# 2        60    103       135     340.0
# 3        45    109       175     282.4
# 4        45    117       148     406.0

# wyswietlenie ostatnich wierszzy 5
print(df.tail())
#      Duration  Pulse  Maxpulse  Calories
# 164        60    105       140     290.8
# 165        60    110       145     300.4
# 166        60    115       145     310.2
# 167        75    120       150     320.4
# 168        75    125       150     330.4

print(df.info())
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
# None
