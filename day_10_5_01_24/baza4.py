import sqlite3

lista = []
sql_connection = None
try:
    sql_connection = sqlite3.connect("../day_9_4_01_25/sqlite_python.db")
    sql_connection.row_factory = sqlite3.Row  # ustawienie aby baza zwracała dane jako słownik
    cursor = sql_connection.cursor()
    print("Baza danych została podłączona")

    select = """
    SELECT * FROM software;
    """
    for row in cursor.execute(select):
        print(row)
        lista.append(dict(row))
    print(lista)
    # [{'id': 1, 'name': 'Python', 'price': 100.0},
    # {'id': 2, 'name': 'Java', 'price': 1000.0},
    # {'id': 3, 'name': 'C++', 'price': 12000.0}]

    # inne podejscie do select
    cursor.execute(select)
    # """ Fetches all rows from the resultset. """
    rows = cursor.fetchall()  # odczytanie danych pobranych z bazy danych
    for row in rows:
        print(dict(row))

    # {'id': 1, 'name': 'Python', 'price': 100.0}
    # {'id': 2, 'name': 'Java', 'price': 1000.0}
    # {'id': 3, 'name': 'C++', 'price': 12000.0}

except sqlite3.Error as e:
    print("Błąd bazy danych", e)
finally:
    if sql_connection:
        sql_connection.close()
        print("Baza danych zostałą zamknięta")
