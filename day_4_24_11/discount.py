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
