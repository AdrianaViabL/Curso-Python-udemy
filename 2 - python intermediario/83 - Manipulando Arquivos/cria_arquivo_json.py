# usando json para alterar dados em arquivos
import json

d1 = {
    "pesssoa 1": {
         'nome':
         'Maria',
         'idade': 25
         },
    "pesssoa 2": {
         'nome':
         'João',
         'idade': 32
         },
}

d1_json = json.dumps(d1, indent=True)

with open('abc.json', 'w+') as file:
    file.write(d1_json)