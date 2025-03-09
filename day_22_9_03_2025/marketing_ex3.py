import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("marketing_r.csv", sep=",")

# "converted" jaki ma typ?
print(df['converted'].dtype)  # object

# zamienic kolumne na typ danych bool
df['converted'] = df['converted'].astype('bool')
print(df['converted'].dtype)  # bool
df.info()
print(df.head(1).to_string())

subscribed = df.groupby(['date_subscribed'])["user_id"].nunique()
retained = df[df['is_retained'] == True].groupby(['date_subscribed'])['user_id'].nunique()

daily_retention_rate = retained / subscribed
print(print("Daily retention rate:", round(daily_retention_rate * 100, 2), "%"))

# dodanie indeksu
daily_retention_rate = pd.DataFrame(daily_retention_rate.reset_index())
print(daily_retention_rate.head())

# zmiana nazw kolumn
daily_retention_rate.columns = ['date_subscribed', 'retention_rate']
print(daily_retention_rate.head())

daily_retention_rate.plot('date_subscribed', 'retention_rate')

plt.title("Dzienny wykres", size=16)
plt.ylabel("Wskażnik utrzymania (%)", size=14)
plt.xlabel("Data", size=14)

plt.ylim(0)  # os y zaczyna sie od 0
plt.show()
