import pandas as pd
import csv

# with open('marketing_przecinek.csv',"r") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)

# df = pd.read_csv("marketing_przecinek.csv", sep=",", engine='python', skipinitialspace=True)
# df = pd.read_csv('marketing_przecinek.csv', delim_whitespace=True)
# df = pd.read_csv('marketing_przecinek.csv', sep=r"\s{2,}", engine='python', skiprows=1)
# df = df.applymap(lambda x: x[:-2] if isinstance(x, str) and x.endswith(".1") else x)
# print(df.head(1).to_string())
# print(df.columns)
# df = df.apply(lambda col: col.apply(lambda x: x[:-2] if isinstance(x, str) and x.endswith(".1") else x))
# print(df.columns)
# df.to_csv('marketing_r.csv', sep=",", index=False)

df = pd.read_csv("marketing_przecinek.csv", sep=",", nrows=1)
print(df)
print(df.columns)
df.columns = df.columns.str.replace(" ", "")
# print(df.columns)

# df_new = df.copy()
# print(df_new)
# print(df_new.columns)
lista_kolumn = df.columns.tolist()
print(lista_kolumn)
df = pd.read_csv('marketing_przecinek.csv',
                 sep=r"\s{2,}",
                 engine='python',
                 skiprows=1,
                 header=None,
                 names=lista_kolumn)
# print(df.head(1).to_string())

# df_new = pd.concat([df_new, df], ignore_index=True)
print(df.head(1).to_string())
df.to_csv('marketing_r.csv', sep=",", index=False)
