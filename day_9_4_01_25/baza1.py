# https://www.sqlite.org/download.html
# sqlite3 test.db  - otworzenie bazy, stworzy nową gdy nie ma
# https://www.heidisql.com
# https://sqlitebrowser.org/dl/
# tworzenie tabeli w bazie danych (sql)
# create table users (id INT PRIMARY KEY, name VARCHAR(100), age INT);
# pokazuje tabele w bazie danych za pomoca silnika sqlite3
# sqlite> .tables  - wyswietla liste tabel
# users
# dodanie uzytkownika do tabeli (sql)
# insert into users (id, name, age) values (1,'Jan Kowalski', 30);
# odczyt danych z tabeli
# select * from users; (sql)
# 1|Jan Kowalski|30
# zmiana danych rekordu
# update users set age=31 where id=1; - zmiana age na 31 dla rekordu o id=1
# usunięcie rekordu (wpisu)
#  delete from users where id=1; - usunięcie elementu o id=1
# wypisanie zawartości kolumnu name z tabeli users
# select name from users;
# wypisz posortowane wg age - kolejnosc rosnąca
# select * from users order by age;
# wypisz posortowane, kolejnosc malejąca - desc
# select * from users order by age desc;
# wypisanie tylko takich, gdzie wiek > 25
# select * from users where age > 25;
# importowanie danych do bazy z pliku csv
# sqlite> create table users(id INT, name TEXT, emali TEXT, age INT);
# sqlite> .mode csv
# sqlite> .import dane_person.csv users
# sqlite>
import sqlite3

sql_connection = None
try:
    sql_connection = sqlite3.connect("sqlite_python.db")
    # sql_connection = sqlite3.connect("../day_9_4_01_25/sqlite_python.db")
    # sql_connection = sqlite3.connect(":memory:") # baza danych w pamięci
    cursor = sql_connection.cursor()
    print("Baza danych została podłączona")
except sqlite3.Error as e:
    print("Błąd bazy danych", e)
finally:
    if sql_connection:
        sql_connection.close()
        print("Baza danych zostałą zamknięta")

# Baza danych została podłączona
# Baza danych zostałą zamknięta
