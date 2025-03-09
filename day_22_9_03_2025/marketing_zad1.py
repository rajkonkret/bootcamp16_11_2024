import pandas as pd
import numpy as np

# df = pd.read_csv('marketing_r.csv')
df = pd.read_csv("marketing_r.csv", sep=",")
print(df.head(1).to_string())
print(df.describe())
df.info()  # nie potrzebuje printa

# "converted" jaki ma typ?
print(df['converted'].dtype)  # object

# zamienic kolumne na typ danych bool
df['converted'] = df['converted'].astype('bool')
print(df['converted'].dtype)  # bool
df.info()
print(df.head(1).to_string())

df["ís_house_ads"] = np.where(df['marketing_channel'] == 'House Ads', True, False)
print(df.ís_house_ads.head(3))
#       user_id date_served marketing_channel          variant  converted language_displayed language_preferred   age_group date_subscribed date_canceled subscribing_channel is_retained
# 0  a100000029      1/1/18         House Ads  personalization       True            English            English  0-18 years          1/1/18           NaN           House Ads        True
# 0    True
# 1    True
# 2    True
# Name: ís_house_ads, dtype: bool

# mapowanie nazw marketing_channel do channel_code
channel_dict = {"House Ads": 1, "Instagram": 2, 'Facebook': 3, "Email": 4, "Push": 5}
df["channel_code"] = df['marketing_channel'].map(channel_dict)
print(df['channel_code'].head(3))
# 0    1.0
# 1    1.0
# 2    1.0
# Name: channel_code, dtype: float64

df['date_served'] = pd.to_datetime(df['date_served'], errors='coerce', format='mixed')
print(df['date_served'].head(3))
# 0   2018-01-01
# 1   2018-01-01
# 2   2018-01-01
# Name: date_served, dtype: datetime64[ns]

# dni tygodnia
# df['date_served'] = df['date_served'].dt.dayofweek
# print(df['date_served'].head(3))

daily_users = df.groupby(["date_served"])["user_id"].nunique()
print("Dziennie:", daily_users)

# narysowac wykres
import matplotlib.pyplot as plt

daily_users.plot()

plt.title("Zasięg dzienny kampani marketingowej")
plt.xlabel("Data")
plt.ylabel("Liczba użytkowników")
plt.xticks(rotation=45)
plt.show()
