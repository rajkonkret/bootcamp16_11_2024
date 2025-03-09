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

language_age = df.groupby(['language_preferred', "age_group"])["user_id"].count()
language_age = pd.DataFrame(language_age.unstack(level=0))
print(language_age.head())
# language_preferred  Arabic  English  German  Spanish
# age_group
# 0-18 years              19     1421      31       68
# 19-24 years             26     1560      29       67
# 24-30 years             19     1442      35       72
# 30-36 years             19     1251      16       69
# 36-45 years             19     1260      19       55

# wykres słupkowy
language_age.plot(kind='bar')
plt.title("Jezyk w zależności od wieku")
plt.xlabel("wiek")
plt.ylabel("Użytkownicy")
plt.legend(loc="upper right", labels=language_age.columns.values)

plt.show()

language_age = df.groupby([ "age_group", 'language_preferred'])["user_id"].count()
language_age = pd.DataFrame(language_age.unstack(level=0))
print(language_age.head())

language_age.plot(kind='bar')
plt.title("Jezyk w zależności od wieku")
plt.xlabel("wiek")
plt.ylabel("Użytkownicy")
plt.legend(loc="upper right", labels=language_age.columns.values)

plt.show()