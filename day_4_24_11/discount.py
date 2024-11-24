from datetime import date, timedelta, datetime

today = date.today()
print(today)  # 2024-11-24
print(type(today))  # <class 'datetime.date'>

time = datetime.now()
print(time)  # 2024-11-24 10:33:04.728631
print(type(time))  # <class 'datetime.datetime'>

print("Godzina", time.hour)
print("Dzień", today.day)
# Godzina 10
# Dzień 24

formatted_date = datetime.now().strftime("%d/%m/%Y")
print("Dzisiejsza data", formatted_date)  # Dzisiejsza data 24/11/2024

# 10:45 zrobić w pythonie
formatted_time = datetime.now().strftime("%H:%M")
print("Aktualna godzina", formatted_time)  # Aktualna godzina 10:46 -> 09:46 -> 9:46
print("Aktualna godzina", formatted_time.removeprefix("0"))  # Aktualna godzina 10:46 -> 09:46 -> 9:46

# praca domowa w formacie 12h 10:45 am

# tomorrow = today + 1# TypeError: unsupported operand type(s) for +: 'datetime.date' and 'int'
#  days=0, seconds=0, microseconds=0,
#                 milliseconds=0, minutes=0, hours=0, weeks=0
tomorrow = today + timedelta(days=1)
print(tomorrow)  # 2024-11-25
products = [
    {'sku': 1, 'exp_date': today, 'price': 100.00},
    {'sku': 2, 'exp_date': today, 'price': 200.00},
    {'sku': 3, 'exp_date': tomorrow, 'price': 250},
    {'sku': 4, 'exp_date': today, 'price': 50},
    {'sku': 5, 'exp_date': today, 'price': 500.00},
]

# print(products)
for product in products:
    # print(product)  # {'sku': 5, 'exp_date': datetime.date(2024, 11, 24), 'price': 500.0}
    # print(product['exp_date'])  # 2024-11-24

    if product['exp_date'] != today:
        continue  # konczy bieżąće wykonanie pętli, bierze kolejny element
        # pass # nic nie rób, idź dalej
    product['price'] *= 0.7  # price = price * 0.7
    print(f"""
Price for sku {product['sku']}
is now {product['price']}
""")
# Price for sku 1
# is now 70.0
#
#
# Price for sku 2
# is now 140.0
#
#
# Price for sku 4
# is now 35.0
#
#
# Price for sku 5
# is now 350.0
