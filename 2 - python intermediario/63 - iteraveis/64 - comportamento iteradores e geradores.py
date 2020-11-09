#lists, tuplas, strings -> sequencias -> iteraveis
nome = 'nome qualquer'
print('comportamento esperado de um valor iteravel')
print('o valor vai sempre estar la para ser exibido novamente')
for l in nome:
    print(l)
print(nome)

print(10 * '=====')


iterador = iter(nome)

try:  # quando mostrado x valor de um iterador, o valor nao existe mais nessa variavel
    print(next(iterador))  # n
    print(next(iterador))  # o
    print(next(iterador))  # m
    print(next(iterador))  # e
    print(next(iterador))
except:
    pass

print('CADE OS VALORES???')
for i in iterador:
    print(i)
print('\ntrabalhando com gerador\n')
gerador = (letra for letra in nome)

print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))

print(10 * '======')

for i in gerador:
    print(i)
