import requests
import json

outcome = []

def makeReq(id):
    url = 'https://pokeapi.co/api/v2/pokemon/'
    response = requests.get(f"{url}{id}/")

    if response.status_code == 200:
        data = response.json()
        relevantData = {
            'id': data['id'],
            'name': data['name'],
            'types': data['types']
        }
        return relevantData
    else:
        print(f"Error: {response.status_code}")

for i in range(1,3):
    outcome.append(makeReq(i))

print(outcome)