import pandas as pd

df = pd.read_csv("marketing_r.csv", sep=",")

# "converted" jaki ma typ?
print(df['converted'].dtype)  # object

# zamienic kolumne na typ danych bool
df['converted'] = df['converted'].astype('bool')
print(df['converted'].dtype)  # bool
df.info()
print(df.head(1).to_string())

subscribers = df[df['converted'] == True]['user_id'].nunique()
total = df['user_id'].nunique()

conv_rate = subscribers / total
print("Convert rate:", round(conv_rate * 100, 2), "%")  # Convert rate: 14.09 %

retained = df[df["is_retained"] == True]["user_id"].nunique()
retention = retained / subscribers
print("Retention rate:", round(retention * 100, 2), "%")  # Retention rate: 65.83 %

# House Ads
house_ads = df[df["subscribing_channel"] == "House Ads"]
retained = house_ads[house_ads["is_retained"] == True]["user_id"].nunique()
subscribers = house_ads[house_ads['converted'] == True]['user_id'].nunique()
retension_rate = retained / subscribers
print("Retention rate:", round(retension_rate * 100, 2), "%")  # Retention rate: 58.05 %

retained = df[df["is_retained"] == True].groupby(['subscribing_channel'])["user_id"].nunique()
print(retained)

subscribers = df[df["converted"] == True].groupby(['subscribing_channel'])["user_id"].nunique()
print(subscribers)

channel_retention_rate = (retained / subscribers) * 100
print(channel_retention_rate)
# subscribing_channel
# Email        87.577640
# Facebook     68.778281
# House Ads    58.053691
# Instagram    68.103448
# Push         70.129870
# Name: user_id, dtype: float64
import matplotlib.pyplot as plt

channel_retention_rate.plot(kind="bar")
plt.title("Wskaźnik utrzymania wg kanału")
plt.xlabel("Kanał", size=14)
plt.ylabel("Konwersja (%)", size=14)
plt.xticks(rotation=45)
plt.show()
