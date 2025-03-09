import pandas as pd
import csv



# with open('marketing_przecinek.csv',"r") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)


# df = pd.read_csv('marketing_przecinek.csv', delim_whitespace=True)
df = pd.read_csv('marketing_przecinek.csv', sep=r"\s+")
print(df)

df.to_csv('marketing_r.csv', sep=",", index=False)