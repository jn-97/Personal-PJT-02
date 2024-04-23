import requests

url = 'http://127.0.0.1:8000/api/auth'

response = requests.post(url, data = {'username' : 'admin', 'password' : '1234'})

print(response.text)

myToken = response.text

header = {'Authorization': 'Token 7151bf03306ce981528665dad68b7a0d8e7e1aa1'}
response = requests.get('http://127.0.0.1:8000/api/post_list', headers=header)
print(response.text)