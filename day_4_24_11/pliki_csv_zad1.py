# pliki csv - dane oddzielone znakiem podziału
# ,;tab
# imię,opis,ocena
# Andrzej Nowak,fajny,4
# "Jan Wiśniewski","fajny","2"
# Kowalski,"wiecznie pyta ""która godzina"", ale może być",5
import csv

row = ['Radek', 'Coe', '3', '0']
fields = ['name', 'branch', 'year', 'cgpa']

zipped_dict = dict(zip(fields, row))
print(zipped_dict)  # {'name': 'Radek', 'branch': 'Coe', 'year': '3', 'cgpa': '0'}

# with open("dane\\records.csv", 'w') as csv_f: - dla windows
with open("dane/records.csv", 'w', newline="") as csv_f:
    csvwriter = csv.writer(csv_f)  # narzędzie do zapisu plików csv
    csvwriter.writerow(row)

# zapis kilku wierszy
with open("dane/records_2.csv", 'w', newline="") as csv_f:
    csvwriter = csv.writer(csv_f)  # narzędzie do zapisu plików csv
    csvwriter.writerow(fields)
    csvwriter.writerow(row)

with open("dane/records_3.csv", 'w', newline="") as csv_f:
    csv_dict_writer = csv.DictWriter(csv_f, fieldnames=fields)
    csv_dict_writer.writeheader()  # zapisz nazwy kolumn
    csv_dict_writer.writerow(zipped_dict)  # zapis jedego słownika jako wiersz

products = [
    {'sku': 1, 'exp_date': 'today', 'price': 100.00},
    {'sku': 2, 'exp_date': 'today', 'price': 200.00},
    {'sku': 3, 'exp_date': 'tomorrow', 'price': 250},
    {'sku': 4, 'exp_date': 'today', 'price': 50},
    {'sku': 5, 'exp_date': 'today', 'price': 500.00},
]
# wyciągnięcie nazw kolumn ze słownika
# products[0] wyciąga z listy pojedynczy słownik
fields_product = [k for k in products[0]]

with open("dane/records_discount.csv", 'w', newline="") as csv_f:
    csv_dict_writer = csv.DictWriter(csv_f, fieldnames=fields_product, delimiter=";")
    csv_dict_writer.writeheader()  # zapisz nazwy kolumn
    csv_dict_writer.writerows(products)  # s - zapis listy słownikó jako kolejne wiersze csv
