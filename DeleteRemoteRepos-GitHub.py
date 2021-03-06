import requests, json

user = 'EnergyWork'
repo = 'test-01'
token = ''
headers = { 
    'Authorization' : f'token {token}',
    'Accept': 'application/vnd.github.v3+json' 
}
url = f'https://api.github.com/repos/{user}/{repo}'
response = requests.delete(url=url, headers=headers)
if response.status_code == 204:
    print('Status:', response.status_code, 'Deleted')
else:
    print('Error', response.status_code)
