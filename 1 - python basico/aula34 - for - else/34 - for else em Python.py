'''

for/else em python

'''

variavel = ['adriana', 'manoel', 'joaozinho', 'maria']

tem_j = False

for valor in variavel:
    if valor.startswith('j'):
        continue
    print(valor)
else:
    print('Não existe uma palavra que começa com J.')