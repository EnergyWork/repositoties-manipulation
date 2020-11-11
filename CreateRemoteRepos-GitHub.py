import requests, json

#* github token: d18de929b6321cf47642ad75593d0756d7905df3

token = 'd18de929b6321cf47642ad75593d0756d7905df3'
headers = { 
    'Authorization' : f'token {token}',
    'Accept': 'application/vnd.github.v3+json' 
}
name = 'Test-01'
description = 'Create a new repository'
repos_url = 'https://api.github.com/user/repos'
data = {
  'name': name,
  'description': description,
  'homepage': 'https://github.com',
  'private': False,
  'auto_init' : True
}
response = requests.post(repos_url, data=json.dumps(data), headers=headers)
if response.status_code == 201:
    resp = response.json()
    print(resp['name'])
    print(resp['owner']['login'])
    print(resp['html_url'])
else:
    print('Error', response.status_code)
