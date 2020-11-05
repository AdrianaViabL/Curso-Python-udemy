"""
são conjuntos de informações como as listas e tuplas,
mas nao tem chave nem indice
"""

s1 = set()
s1.add(1)
s1.add(2)
s1.add(3)
print(s1)
s1.discard(2)

print('apos deletar um dado da', s1)

s1.update('testando')  # ele nao aceita elementos duplicados, entao o 't' so vai aparecer uma vez

print(s1)

l1 = [1, 2, 2, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 'nome', 'nome']
l1 = set(l1)
print(l1)
print(10 * '-----')
print('usando intersection(&) difference(-) symmetric_difference(^)')

s1 = {1, 2, 3, 4, 5}
s2 = {1, 2, 3, 4, 5, 6}
s3 = s1 | s2  #  juntando dois conjuntos

print('\njuntando dois conjuntos com | ', s3)

s4 = s1 & s2
print('\njuntando dois conjuntos com & ', s4)

s1.add(7)
s5 = s1 - s2

print('\ndiferenca entre os conjuntos ', s5)

s6 = s1 ^ s2

print('\npegando valores que existem sem repetição \nnos dois sets ', s6)


