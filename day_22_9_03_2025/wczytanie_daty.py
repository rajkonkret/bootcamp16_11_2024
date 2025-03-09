import pandas as pd

df = pd.read_csv("marketing_r.csv",
                 sep=",",
                 parse_dates=['date_served',
                              "date_subscribed",
                              "date_canceled"])

print(df.to_string())
