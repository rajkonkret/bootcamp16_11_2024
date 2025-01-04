import requests

url = 'http://numbersapi.com/random/year?json'

response = requests.get(url)
data = response.json()
print(data)
print(type(data))
# {'text': '703 is the year that Elias I becomes Catholicos of Armenia.',
#  'number': 703,
#  'found': True, 'type': 'year'}
print("Podaj odpowiedź na pytanie:\n", data['text'].replace(str(data['number']), ""))
odp = input()  # str
if odp == str(data['number']):
    print("Prawidłowa odpowiedź")
else:
    print("Błąd")
