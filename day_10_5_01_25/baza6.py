import sqlite3

sql_connection = None
try:
    sql_connection = sqlite3.connect("../day_9_4_01_25/sqlite_python.db")
    cursor = sql_connection.cursor()
    print("Baza danych została podłączona")

    update = '''
    UPDATE software SET price=1999 where id=7;
    '''

    # cursor.execute(update)
    # sql_connection.commit()

    delete = """
    DELETE FROM software WHERE id=1;
    """

    # cursor.execute(delete)
    # sql_connection.commit()

    select = """
    SELECT * FROM software WHERE price > 2000;
    """

    cursor.execute(select)
    rows = cursor.fetchall()
    for r in rows:
        print(r)
except sqlite3.Error as e:
    print("Błąd bazy danych", e)
finally:
    if sql_connection:
        sql_connection.close()
        print("Baza danych zostałą zamknięta")

# Baza danych została podłączona
# (3, 'C++', 12000.0)
# (4, 'Scala', 5600.0)
# Baza danych zostałą zamknięta
