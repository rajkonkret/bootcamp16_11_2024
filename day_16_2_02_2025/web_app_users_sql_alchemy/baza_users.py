import sqlite3

try:
    conn = sqlite3.connect("data/cantor.db")
    c = conn.cursor()

    query = '''
    CREATE TABLE IF NOT EXISTS transactions (
    id INTEGER PRIMARY KEY,
    currency TEXT,
    amount INTEGER,
    user TEXT);
    '''

    # c.execute(query)
    # conn.commit()

    create_users = '''CREATE TABLE IF NOT EXISTS users(
    id integer primary key autoincrement,
    name varchar(100) not null unique,
    email varchar(100) not null unique,
    password text,
    is_active boolean not null default 0,
    is_admin boolean not null default 0
    );'''

    c.execute(create_users)
    conn.commit()

except sqlite3.Error as e:
    print("Bład", e)
finally:
    if conn:
        conn.close()
