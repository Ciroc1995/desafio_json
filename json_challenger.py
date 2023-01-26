import json

with open('desafio.json') as arquivo_json:
    data = json.load(arquivo_json)
    print(data['user'][1]['email'])
    print(data['user'][0]['address']['city'])
    print(data['user'][1]['orders'][0]['total'])
