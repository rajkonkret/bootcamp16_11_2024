import sqlite3

data = [
    (5, "Rust", 899),
    (6, "Angular", 1899),
    (7, "JS", 99),
]

sql_connection = None
try:
    sql_connection = sqlite3.connect("../day_9_4_01_25/sqlite_python.db")
    cursor = sql_connection.cursor()
    print("Baza danych została podłączona")

    insert = """
    INSERT INTO software (id,name,price) VALUES (?,?,?);
    """

    # wpiaywanie podstawionych danych do bazy danych
    # cursor.execute(insert, (4, "Scala", 5600))
    # sql_connection.commit()

    # wrzucenie do bazy danych z listy odpowiadającej rekordom w bazie
    cursor.executemany(insert, data)
    sql_connection.commit()

except sqlite3.Error as e:
    print("Błąd bazy danych", e)
finally:
    if sql_connection:
        sql_connection.close()
        print("Baza danych zostałą zamknięta")
