import requests

client_id = ""
scope = "public"
auth_url = f"https://dribbble.com/oauth/authorize?client_id={client_id}"
print(f"Otwóz poniższy URL w przeglądarce aby się zalogować:\n {auth_url}")

# uzyskany kod
code = ""
# response = requests.get(auth_url)
# print(response.text)
