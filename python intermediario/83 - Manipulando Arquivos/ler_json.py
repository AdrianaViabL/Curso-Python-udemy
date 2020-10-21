#fazendo com que o arquivo voltar a ser um dicionario

import json

with open('abc.json', 'r') as file:
    d1_json = file.read()
    d1_json = json.loads(d1_json)
    print('acessando o arquivo json gerado anteriormente \n'
          'e transformando em um dicionario')
    print(d1_json)

for k, v in d1_json.items():
    print(k)
    for k1, v1 in v.items():
        print(k1, v1)
