#o valor da chave deve ser unico

d1 = {'chave1': 'valor da chave', 'chave2': 12}
print('antes de tentar pegar uma chave que nao existe: ', d1)

print(d1.get('chave nao existe'))#forma de tentar pegar um valor de chave que nao existe
print(d1)

d1['chave nova'] = 'valo novo da chave'
print('primeira forma de acrescentar valor a um dicionario')
d1.update({'nova':'novo valor'})

print('segunda forma de acrescentar valor a um dicionario')

del d1['chave1']
print('apos a exclusao: ', d1)

print('valor' in d1.values())  # checando se o valor 'valor'existe dentro do dicionario

print(len(d1))

print(10 * '====')
print('acessando as chaves do dicionario')
for k in d1:
    print(k)

print('acessando so o valor do dicionario')
for k in d1.values():
    print(k)
print(10 * '====')
print('acessando tanto a chave como o valor')
for k, v in d1.items():
    print(k, v)

v = d1.copy()
print(10 * '====')
v['nova'] = 'qualquer'
print(v)
print(d1)

