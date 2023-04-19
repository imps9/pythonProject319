import requests
import json

status='available'
res = requests.get(f"https://petstore.swagger.io/v2/pet/findByStatus?status={status}", headers = {'accept': 'application/json'})
print(res.text)
print(res.json())

# post user
# base_url = 'https://petstore.swagger.io/v2'
data = {
    "id": 0,
    "username": "Alu",
    "firstName": "Nord",
    "lastName": "Alex",
    "email": "sim@email.ru",
    "password": "12345",
    "phone": "8-911-911-11-11",
    "userStatus": 0
}
headers = {'accept': 'application/json',
           'Content-Type': 'application/json'}
new_user = requests.post(f'https://petstore.swagger.io/v2/user', json=data, headers=headers)

data = json.dumps(data)

print(new_user.status_code)
print(new_user.json())

# get user
username = 'Alu'
res = requests.get(f"https://petstore.swagger.io/v2/user/{username}", headers={'accept': 'application/json'})
print(res.text)
print(res.json())

# Put user
username = 'Alu'
data = {
    "id": 0,
    "username": "Alu",
    "firstName": "west",
    "lastName": "Alex",
    "email": "sim@email.ru",
    "password": "12345",
    "phone": "8-911-911-11-11",
    "userStatus": 0
}
headers = {'accept': 'application/json',
           'Content-Type': 'application/json'}
new_user1 = requests.put(f'https://petstore.swagger.io/v2/user/{username}"', json=data, headers=headers)

data = json.dumps(data)

print(new_user1.status_code)
print(new_user1.json())

# DELETE User
username = 'Alu'
res = requests.delete(f"https://petstore.swagger.io/v2/user/{username}", headers={'accept': 'application/json'})
print(res.status_code)
print(res.json())


