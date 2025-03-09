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

df.to_csv("marketing_r_bool.csv", index=False)
df = pd.read_csv("marketing_r_bool.csv", sep=",")

# "converted" jaki ma typ?
print("Converted column", df['converted'].dtype)  # object

# retention_total = df['user_id'].nunique()
retention_total = df.groupby(['date_subscribed', "subscribing_channel"])["user_id"].nunique()
retention_subs = df[df['is_retained'] == True].groupby(['date_subscribed', "subscribing_channel"])["user_id"].nunique()
print(retention_subs.head(3))

retention_rate = retention_subs / retention_total
print(retention_rate)

retention_rate = pd.DataFrame(retention_rate.unstack(level=1))
print(retention_rate)
retention_rate.plot()
plt.title("data w zależności od kanału")
plt.xlabel("Data")
plt.ylabel("Użytkownicy")
plt.legend(loc="upper right", labels=retention_rate.columns.values)

plt.show()
