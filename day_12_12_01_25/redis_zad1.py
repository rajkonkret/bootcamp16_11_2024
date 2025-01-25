# Redis (IPA: rɛdɪs; skrót od nazwy Remote Dictionary Server[6]) – otwartoźródłowe[3]
# oprogramowanie działające jako nierelacyjna baza danych przechowująca
# dane w strukturze klucz-wartość w pamięci operacyjnej serwera,
# docker pull redis
# docker run --name redis-server -d -p 6379:6379 redis
import redis

# pip install redis==4.5.3
# pip install redis --upgrade

# połączenie do bazy Redis (localhost, port 6379)
r = redis.Redis()

# ustawienie wartości klucza
r.set('name', 'Radek')

# pobieranie wartości klucza
wartosc = r.get('name')
print(wartosc)  # b'Radek'
print(wartosc.decode('utf-8'))

# usunięcie klucza
r.delete('name')

czy_istnieje = r.exists('name')
print(czy_istnieje)
