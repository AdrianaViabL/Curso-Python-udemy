from dados import pessoas, qualquercoisa, produtos
from functools import reduce


soma_lista = reduce(lambda acumulador, item: item + acumulador, qualquercoisa, 0)
print(soma_lista)
print(10 * '===')

soma_preco = reduce(lambda ac, p: p['preco'] + ac, produtos, 0)
print(f'soma dos precos {round( soma_preco, 2)}')


soma_idade = reduce(lambda ac, p:p['idade'] + ac, pessoas, 0)

print(round(soma_idade / len(pessoas)), 2)

