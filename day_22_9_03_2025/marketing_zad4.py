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

language = df.groupby(['date_served', "language_preferred"])["user_id"].count()
print(language.head())
# date_served  language_preferred
# 1/1/18       Arabic                  4
#              English               355
#              German                  5
#              Spanish                11
# 1/10/18      Arabic                  1
language = pd.DataFrame(language.unstack(level=1))
print(language.head())
# language_preferred  Arabic  English  German  Spanish
# date_served
# 1/1/18                 4.0    355.0     5.0     11.0
# 1/10/18                1.0    315.0     5.0     21.0
# 1/11/18                9.0    287.0     2.0     16.0
# 1/12/18                4.0    287.0     4.0     11.0
# 1/13/18                8.0    278.0     5.0     17.0

language.plot()
plt.title("Dzienne preferencje językowe")
plt.xlabel("Data")
plt.ylabel("Użytkownicy")
plt.legend(loc="upper right", labels=language.columns.values)

plt.show()
