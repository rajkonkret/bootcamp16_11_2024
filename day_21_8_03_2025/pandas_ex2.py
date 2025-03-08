import pandas as pd

df = pd.read_csv('data.csv')
print(df)  # wyswietli 5 początkowych i 5 końcowych wierszy
#      Duration  Pulse  Maxpulse  Calories
# 0          60    110       130     409.1
# 1          60    117       145     479.0
# 2          60    103       135     340.0
# 3          45    109       175     282.4
# 4          45    117       148     406.0
# ..        ...    ...       ...       ...
# 164        60    105       140     290.8
# 165        60    110       145     300.4
# 166        60    115       145     310.2
# 167        75    120       150     320.4
# 168        75    125       150     330.4

# wyswietlenie wszystkich danych
print(df.to_string())

# maksymalna liczba wyswietlanych wierszy, jesli wiecej wyswietla dane cząstkowe
print(pd.options.display.max_rows)  # 60

pd.options.display.max_rows = 9999  # ustawienie limitu cząstkowych danych na 9999 wierszy
print(df)
pd.options.display.max_rows = 60
