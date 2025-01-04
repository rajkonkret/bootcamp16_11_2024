# url = "https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API key}"
import requests
from datetime import datetime
url = "https://api.openweathermap.org/data/2.5/weather?q=Warszawa&appid={API key}&&lang=pl&format=jsonl&units=metric"

page = requests.get(url)
print(page)  # <Response [200]>
print(page.text)

data = page.json()
print(data)
# {'coord': {'lon': 21.0118, 'lat': 52.2298},
#  'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}],
#  'base': 'stations',
#  'main':
#   {'temp': -1.54, 'feels_like': -7.49, 'temp_min': -2.32, 'temp_max': -0.44, 'pressure': 1016, 'humidity': 75,
#           'sea_level': 1016, 'grnd_level': 1004}, 'visibility': 10000, 'wind': {'speed': 6.17, 'deg': 280},
#  'clouds': {'all': 20}, 'dt': 1735982207,
#  'sys': {'type': 2, 'id': 2032856, 'country': 'PL', 'sunrise': 1735973073, 'sunset': 1736001414}, 'timezone': 3600,
#  'id': 756135, 'name': 'Warsaw', 'cod': 200}
print(data['weather'][0]['description'])  # few clouds, pochmurnie
print(data['main']['temp'])  # -1.5
print(data['main']['temp_min'])  # -2.26
print(data['main']['temp_max'])  # -0.44
print(data['name']) # Warszawa
# sunrise, sunset
print("-------")
sunrise = data['sys']['sunrise']
print("Wschód słońca", sunrise) # Wschód słońca 1735973073
# timestamp - liczba sekund od epoki Unixa - 1 stycznia 1970
dt_object_sunrise = datetime.fromtimestamp(sunrise)
print("Wschód słońca", dt_object_sunrise) # Wschód słońca 2025-01-04 07:44:33
print("-----")
print(5 * "-")
sunset = data['sys']['sunset']
dt_object_sunset = datetime.fromtimestamp(sunset)
print("Zachód słońca", sunset)
print("Zachód słońca", dt_object_sunset)
# -------
# Wschód słońca 1735973073
# Wschód słońca 2025-01-04 07:44:33
# -----
# -----
# Zachód słońca 1736001414
# Zachód słońca 2025-01-04 15:36:54