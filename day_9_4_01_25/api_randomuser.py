import requests as re
from pydantic import BaseModel

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
class Name(BaseModel):
    title: str
    first: str
    last: str


class Picture(BaseModel):
    large: str


class UserInfo(BaseModel):
    # name: dict
    name: Name
    email: str
    picture: Picture


user = data['results'][0] # wyciągnięcie usera z listy
user_info = UserInfo(**user) # rozpakowanie słownika na obiekty
print(user_info)
# name = {'title': 'Mademoiselle', 'first': 'Emmanuelle', 'last': 'Marie'}
# email = 'emmanuelle.marie@example.com'
# picture = {'large': 'https://randomuser.me/api/portraits/women/78.jpg',
#            'medium': 'https://randomuser.me/api/portraits/med/women/78.jpg',
#            'thumbnail': 'https://randomuser.me/api/portraits/thumb/women/78.jpg'}

# Po uzupełnieniu modelu klas
# name = Name(title='Mr', first='Helge', last='Lillegård')
# email = 'helge.lillegard@example.com'
# picture = Picture(large='https://randomuser.me/api/portraits/men/26.jpg')
print(f"Imię: {user_info.name.first}")
print(f"Nazwisko: {user_info.name.last}")
print(f"Email: {user_info.email}")

photo_url_pydantic = user_info.picture.large
print(f"Link do zdjęcia: {photo_url_pydantic}")  # Link do zdjęcia: https://randomuser.me/api/portraits/men/21.jpg
response_photo_pydantic = re.get(photo_url_pydantic)
with open("user_photo_pydantic.jpg", "wb") as f:
    f.write(response_photo_pydantic.content)
print("Zdjęcie zostało zapisane")
