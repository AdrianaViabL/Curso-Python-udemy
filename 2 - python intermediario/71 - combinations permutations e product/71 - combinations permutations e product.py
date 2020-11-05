"""
combinations, permutations e product - itertools
combinations - ordem nao importa
permutations - ordem importa, os valores se 'repetem' sendo so a posição que muda
ambos nao repetem valores unicos nas linhas de combinação
product - ordem importa e repete valores unicos
"""
from itertools import combinations, permutations, product
pessoa = ['Luiz', 'André', 'Eduardo', 'Letícia', 'Fabricio', 'Rose']

for grupo in combinations(pessoa, 2):
    print(grupo)

print(10 * '=====')

for grupo in permutations(pessoa, 3):
    print(grupo)

print(10 * '=====')

for grupo in product(pessoa, repeat=2):
    print(grupo)

