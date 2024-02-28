import requests

headers = {
    "Authorization": "Bearer " + "YOUR_TOKEN_HERE",
    "Content-Type": "application/json"
}

response = requests.post("http://127.0.0.1:8000/user/verify", headers=headers)
print(response.json())
