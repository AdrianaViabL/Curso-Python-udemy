'''
quando se trabalha com groupby os dados devem estar ordenados
para que ele consiga agrupar todos iguais em um dicionario
'''

from itertools import groupby
alunos = [
    {'nome': 'Adriana', 'nota': '10'
    },
    {'nome': 'Eragon', 'nota': '5'
    },
    {'nome': 'João', 'nota': '7'
    },
    {'nome': 'Maria', 'nota': '7'
    }
]

alunos.sort(key=lambda item:item['nota'])

alun_agrupado = groupby(alunos, lambda item:item['nota'])
print('vendo a chave e o agrupamento antes de ser desempacotado')
for agrupamento, vl_agrupado in alun_agrupado:
    print(f'agrupamento {agrupamento}')
    qtd = len(list(vl_agrupado))
    print(f'{qtd} alunos tiraram {agrupamento}')

print('é gerado um iterador, entao o valor ja foi "usado no primeiro FOR"')
for grupo in alun_agrupado:
    print(grupo)

