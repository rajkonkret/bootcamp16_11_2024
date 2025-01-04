import requests as re

url = "https://randomuser.me/api/"

response = re.get(url)
print(response)  # <Response [200]>
print(response.text)
data = response.json()

user = data['results'][0]
print(user)
print(f"Osoba: {user['name']}")
# Imię: {'title': 'Mrs', 'first': 'Sema', 'last': 'Heuvelink'}
print(f"Imię: {user['name']['first']}")
print(f"Nazwisko: {user['name']['last']}")
# Imię: Frederikke
# Nazwisko: Sørensen
print(f"Numer telefonu: {user['phone']}")  # Numer telefonu: 911-564-046
photo_url = user['picture']['large']
print(f"Link do zdjęcia: {photo_url}")
# Link do zdjęcia: https://randomuser.me/api/portraits/women/44.jpg

response_photo = re.get(photo_url)
print(response_photo)  # <Response [200]>
with open("user_photo.jpg", "wb") as f:
    f.write(response_photo.content)
print("Zdjęcie zostało zapisane")

# zbudować schemat klas dla name(first, last), email, picture(large)
