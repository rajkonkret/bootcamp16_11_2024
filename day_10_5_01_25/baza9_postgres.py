import psycopg2

# uruchomienie bazy danych postgress
# docker run --name my-postgres -e POSTGRES_USER=myuser -e POSTGRES_PASSWORD=mypassword -e POSTGRES_DB=mydatabase -p 5432:5432 -d postgres
# docker ps - lista aktywnych kontenerów
# docker ps -a - lista wszystkich kontenerów (aktywnych i  nieaktywnych)
# docker stop my-postgres - zatrzymania kontera o nazwie my-postgres
# docker start my-postgres - wznowienie kontenera o nazwie my-postgres
# pip install psycopg2
# psql -U myuser -d mydatabase - logowanie do bazy postgres z konsoli
# pgAdmin - program do zarządznia bazą postgres
# "localhost" (127.0.0.1)

conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="mydatabase",
    user="myuser",
    password="mypassword"
)

cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS users (id SERIAL PRIMARY KEY, name TEXT, email TEXT);")
conn.commit()

cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", ("Jan", "jan@rajkonkret.pl"))
cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", ("Anna", "anna@rajkonkret.pl"))
conn.commit()

cursor.execute("SELECT * FROM users")
for row in cursor.fetchall():
    print(row)

cursor.close()
conn.close()
# (1, 'Jan', 'jan@rajkonkret.pl')
# (2, 'Anna', 'anna@rajkonkret.pl')
# (3, 'Jan', 'jan@rajkonkret.pl')
# (4, 'Anna', 'anna@rajkonkret.pl')
