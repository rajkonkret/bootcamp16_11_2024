import sqlite3

sql_connection = None
try:
    sql_connection = sqlite3.connect("../day_9_4_01_25/sqlite_python.db")
    # sql_connection = sqlite3.connect(":memory:")  # baza danych w pamięci
    cursor = sql_connection.cursor()
    print("Baza danych została podłączona")

    insert = """
    INSERT INTO software (id,name,price) VALUES(1,'Python',100);
    """

    insert2 = """
      INSERT INTO software (id,name,price) VALUES(2,'Java',1000);
      """

    insert3 = """
      INSERT INTO software (id,name,price) VALUES(3,'C++',12000);
      """

    # dodac dwa inne wpisy

    # cursor.execute(insert)
    # wpisanie kolejnych rekordów
    # cursor.execute(insert2)
    # cursor.execute(insert3)
    # sql_connection.commit()

    select = """
    SELECT * FROM software;
    """

    for row in cursor.execute(select):
        print(row)
# Baza danych została podłączona
# (1, 'Python', 100.0)
# (2, 'Java', 1000.0)
# (3, 'C++', 12000.0)
# Baza danych zostałą zamknięta
except sqlite3.Error as e:
    print("Błąd bazy danych", e)
finally:
    if sql_connection:
        sql_connection.close()
        print("Baza danych zostałą zamknięta")
