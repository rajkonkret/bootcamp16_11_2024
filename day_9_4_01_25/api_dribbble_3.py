import requests

access_token = ""
api_url = "https://api.dribbble.com/v2/user"
headers = {"Authorization": f"Bearer {access_token}"}

response = requests.get(api_url, headers=headers)

if response.status_code == 200:
    user_data = response.json()
    print(user_data)
    print(f"Zalogowany jako: {user_data['name']}")
    print(f"Utworzony: {user_data['created_at']}")
    print(f"Id: {user_data['id']}")
else:
    print("Bład w zapytaniu:", response.json())

# {'avatar_url': 'https:default_avatars/default-avatar-gradient-6.png', 'bio': '',
#  'created_at': '2025-01-03T13:30:27.770-05:00', 'followers_count': 0, 'html_url': 'https://dribbble.com/radekjan',
#  'id': 22791765, 'links': {}, 'location': 'poland', 'login': 'radekjan', 'name': 'radek', 'pro': False, 'type': 'User',
#  'email': 'rajkonkret660@gmail.com', 'can_upload_shot': True, 'teams': []}
# Zalogowany jako: radek
# Utworzony: 2025-01-03T13:30:27.770-05:00
# Id: 22791765