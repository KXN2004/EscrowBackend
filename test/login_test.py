import requests

data = {
    # Add email
    "username": "",
    # Add Phone Number
    "password": ""
}

response = requests.post("http://127.0.0.1:8000/user/login", data=data)

print(response.json())
