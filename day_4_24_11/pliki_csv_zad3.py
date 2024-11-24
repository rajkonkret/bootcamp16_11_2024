import pandas

# pip install pandas

data = pandas.read_csv('dane/records_discount.csv', delimiter=";")
print(data)
#    sku  exp_date  price
# 0    1     today  100.0
# 1    2     today  200.0
# 2    3  tomorrow  250.0
# 3    4     today   50.0
# 4    5     today  500.0

print(data.columns)  # Index(['sku', 'exp_date', 'price'], dtype='object')
