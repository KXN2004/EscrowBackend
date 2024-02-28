import requests

data = {
    "username": "Kevin Nadar",
    "password": "kevin"
}

response = requests.post("http://127.0.0.1:8000/user/login", data=data)

print(response.json())
