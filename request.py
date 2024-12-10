import requests
import json

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
        print(json.dumps(relevantData, indent=2))  # Pretty-print the JSON response
    else:
        print(f"Error: {response.status_code}")

for i in range(0,3):
    makeReq(i)