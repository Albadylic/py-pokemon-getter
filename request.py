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
            'types': data['types'],
            'sprite': data['sprites']['front_default']
        }
        return relevantData
    else:
        print(f"Error: {response.status_code}")

for i in range(1,387):
    outcome.append(makeReq(i))

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(outcome, f, ensure_ascii=False, indent=4)

print('complete')