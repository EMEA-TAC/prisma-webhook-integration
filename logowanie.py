import requests
import json

# Adres URL do logowania
url = "https://api2.eu.prismacloud.io/login"

# Dane logowania
payload = {
    "username": "c7bcb7fb-2ba8-49f3-b052-c7bef3ad11b3",
    "prismaId": "1037390876936064000",
    "password": "aaa"
}

# Nagłówki
headers = {
    'Content-Type': 'application/json'
}

# Wykonywanie żądania POST
response = requests.post(url, headers=headers, data=json.dumps(payload))

# Wypisanie odpowiedzi
print(response.text)

# Sprawdzenie, czy logowanie się powiodło i wypisanie tokena
if response.status_code == 200:
    print("Logowanie powiodło się.")
    token = response.json().get('token')
    print(f"Token: {token}")
else:
    print("Logowanie nie powiodło się.")
