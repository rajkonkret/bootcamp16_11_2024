import redis

# client = redis.Redis(host='localhost', port=6379, db=0)
client = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

client.set('foo', 'barśź')

value = client.get('foo')
# print(value.decode('utf-8')) # barśź
print(value)  # decode_responses=True -> barśź zwraca tekst, poprzednio zwracało byte
