from itertools import zip_longest, count
'''
Zip - unindo iteraveis
Zip_longest - Itertools
'''
cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo', 'qualer']
estado = ['SP', 'MG', 'BA']
ind = count()
cidade_estado = zip(ind, estado, cidades)  # ele elimina o excedente da maior lista
print(type(cidade_estado))

print('\nusando o zip_longest\n')

indice = count()
cid_est = zip_longest(indice,
                      estado,
                      cidades,
                      fillvalue='estado') # ele coloca none onde nao tem valor declarado, ou usando o fillvalue é declarado um valor padrao
print('NAO EXECUTAR com FOR o cid_est, pois por causa do indice count, o programa entra em LOOP')
print('chegou AQUI')
for ind, est, cid in cidade_estado:
    print(ind, est, cid)

