import sqlite3

sql_connection = None
try:
    # sql_connection = sqlite3.connect("sqlite_python.db")
    sql_connection = sqlite3.connect("../day_9_4_01_25/sqlite_python.db")
    # sql_connection = sqlite3.connect(":memory:") # baza danych w pamięci
    sql_connection.row_factory = sqlite3.Row # zwraca dane, które możemy przekształcić na słownik
    cursor = sql_connection.cursor()
    print("Baza danych została podłączona")

    # table_data = 'software'
    table_data = 'hardware'

    select= f"SELECT * FROM {table_data};"

    cursor.execute(select)
    rows = cursor.fetchall()
    for row in rows:
        print(dict(row))

except sqlite3.Error as e:
    print("Błąd bazy danych", e)
finally:
    if sql_connection:
        sql_connection.close()
        print("Baza danych zostałą zamknięta")

# Baza danych została podłączona
# {'id': 2, 'name': 'Java', 'price': 1000.0}
# {'id': 3, 'name': 'C++', 'price': 12000.0}
# {'id': 4, 'name': 'Scala', 'price': 5600.0}
# {'id': 5, 'name': 'Rust', 'price': 899.0}
# {'id': 6, 'name': 'Angular', 'price': 1899.0}
# {'id': 7, 'name': 'JS', 'price': 1999.0}
# Baza danych zostałą zamknięta

# ------
# Baza danych została podłączona
# {'id': 1, 'name': 'samsung', 'price': 8999.0}
# Baza danych zostałą zamknięta