"""
https://docs.python.org/3/library/json.html - documentação
JavaScript Object Notation - JSON
JSON (JavaScript Object Notation) é um formato de troca de dados entre sistemas
e programas muito leve e de fácil utilização. Muito utilizado por APIs

DUMPS / Dump
######################
Python          JSON
dict	        object
list, tuple	    array
str	            string
int, float  	number
True        	true
FALSE	        False
None	        null

LOADS / Load
######################
JSON	        Python
object	        dict
array	        list
string	        str
number (int)	int
number (real)	float
true	        True
false	        False
null	        None
"""
from JSON_dados import *
import json

print(clientes_dicionario)
print('convertendo um dicionario em um objeto JSON')
convertido_json = json.dumps(clientes_dicionario, indent=4)
print(convertido_json)
print(type(convertido_json))
print(10 * "====")

dicionario = json.loads(clientes_json)
for chave, valor in dicionario.items():
    print(chave)
    print(valor)

print('trabalhando com arquivo')
with open('clietes.json', 'w') as arquivo:
    json.dump(clientes_dicionario, arquivo, indent=4)

with open('clietes.json', 'r') as arquivo:
    dados = json.load(arquivo)
print('arquivo convertido de volta em dicionario')
print(dados)
