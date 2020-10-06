"""
Listas em Python
fatiamento
append, insert, pop, del clear, extend,
min, max
range
"""
# indice  0    1    2    3    4
lista = ['A', 'B', 'C', 'D', 10.5]
# neg -   5    4    3    2    1

print(lista)
print(10 * '----')
print('concatenando listas')
l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = l1 + l2

print(f'lista 1 = {l1}')
print(f'lista 2 = {l2}')
print(f'lista 1 e 2 concatenadas com o sinal de + =  {l3}')
print('ou usando o Extend para acrescentar algo em uma lista')
l1.extend(l2)

print(f'lista 1 e 2 juntas na lista 1 = {l1}')
print(10 * '----')
print('eliminando o item final da lista usando "pop"')

l1.pop()
print(f'lista 1 {l1}')
print(10 * '----')
print('usando o del para excluir os itens da lista')
print(f'lista l1 sem os itens do index 2 ate 4')
del(l1[2:4])

print(f'lista 1 {l1}')