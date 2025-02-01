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

    c.execute(query)
    conn.commit()

except sqlite3.Error as e:
    print("Bład", e)
finally:
    if conn:
        conn.close()
