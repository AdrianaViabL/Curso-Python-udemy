'''
trocando valores de variaveis sem a
necessidade de criar uma 3º variavel
'''
x = 1
y = 'nome1111'
print('forma tradicional de transferir um valor de uma variável para a outra')
print(f'valor na var x = {x} --- y = {y}')
a = x
x = y
y = a
print(f'valor depois na x = {x} --- y = {y}')

print('forma possivel no Python')
v1 = 20
v2 = 'cachorro'
print(f'var v1 = {v1} --- v2 = {v2}')
v1, v2 = v2, v1
print(f'var v1 = {v1} ---- v2 = {v2}')
