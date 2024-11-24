import csv

columns = []
rows = []

filename = 'dane/records_3.csv'  # wiele wierszy
# filename = 'dane/records_discount.csv'  # wiele wierszy oddzielone ;

with open(filename, 'r') as f:
    dialect = csv.Sniffer().sniff(f.read(1024))  # odczytalismy 1024 elementy
    print(dialect.delimiter)  # ;
    f.seek(0)  # ponowne ustawienie odczytu pliku na początek
    # csvreader = csv.reader(f, delimiter=";")  # narzedzie do odczytu
    csvreader = csv.reader(f, delimiter=dialect.delimiter)  # narzedzie do odczytu
    print(csvreader)  # <_csv.reader object at 0x000002510ADBE5C0>
    # iterator - można uzywac go sekwencji
    # pobierac po kolei pojedyncze elementy next()
    # StopIteration - wyczerpanie danych z iteratora
    columns = next(csvreader)  # pierwszy wiersz

    for row in csvreader:  # zacznie od drugiego
        # print(row)
        rows.append(row)

print("Columns", columns)
print("Rows", rows)
# Columns ['name', 'branch', 'year', 'cgpa']
# Rows [['Radek', 'Coe', '3', '0']]
# Columns ['sku;exp_date;price']
# Rows [['1;today;100.0'], ['2;today;200.0'], ['3;tomorrow;250'], ['4;today;50'], ['5;today;500.0']]
# Columns ['sku', 'exp_date', 'price']
# Rows [['1', 'today', '100.0'], ['2', 'today', '200.0'],
# ['3', 'tomorrow', '250'], ['4', 'today', '50'], ['5', 'today', '500.0']]
# ;
# <_csv.reader object at 0x000001E21593E5C0>
# Columns ['sku', 'exp_date', 'price']
# Rows [['1', 'today', '100.0'], ['2', 'today', '200.0'], ['3', 'tomorrow', '250'], ['4', 'today', '50'], ['5', 'today', '500.0']]
# ,
# <_csv.reader object at 0x000002560A13E5C0>
# Columns ['name', 'branch', 'year', 'cgpa']
# Rows [['Radek', 'Coe', '3', '0']]