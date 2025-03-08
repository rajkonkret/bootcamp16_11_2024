import pandas as pd

df = pd.read_csv('data.csv')
print(df.corr())
#           Duration     Pulse  Maxpulse  Calories
# Duration  1.000000 -0.155408  0.009403  0.922721
# Pulse    -0.155408  1.000000  0.786535  0.025120
# Maxpulse  0.009403  0.786535  1.000000  0.203814
# Calories  0.922721  0.025120  0.203814  1.000000
