"""
mostrar nome, idade, altura, peso
depois o IMC
depois ano de nascimento
"""
from datetime import datetime
nome = 'João'
idade = 34
peso = 90.0
altura = 1.89
now = datetime.now()
anoAtu = now.year
anoNasc = anoAtu - idade

imc = peso / altura ** 2

print(f'{nome} tem {idade} anos, {altura} de altura e pesa {peso}kg')
print(f'O IMC de {nome} é {imc:.2f}')
print(f'{nome} nasceu em {anoNasc}')