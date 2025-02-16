import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('dane/data.csv')
# print(df)
# print(df['date'])

df['date'] = pd.to_datetime(df.date, format='%d/%m/%Y')
x = df['date']
y = df['Close']

lista = [100, 999]

figura, ax = plt.subplots(2, figsize=(10, 4))
ax[0].scatter(x, y, marker="+", alpha=.5)
_ = ax[1].pie(lista, labels=['wpłata', 'wypłata'])
_ = ax[1].legend()

plt.show()