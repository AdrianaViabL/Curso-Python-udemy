from dados import pessoas, qualquercoisa, produtos

nova_lista = filter(lambda x:x > 5, qualquercoisa) #  usando a função filter
nova_lista2 = [x for x in qualquercoisa if x > 5]  #
print(nova_lista2)
print('\nusando filter com dicionario com produtos\n')

novo_dic = filter(lambda p: p['preco'] > 20, produtos)  #pegando os produtos que custam mais de 20

for i in novo_dic:
    print(i)

print(list(novo_dic))  # dicionario vazio pois ja foi 'usado' o valor dentro do dicionario

print('\nusando filter com dicionario com as pessoas\n')
def filtra(pessoa):
    if pessoa['idade'] < 18:
        return True

novo_pess = filter(filtra, pessoas)

for pess in novo_pess:
    print(pess)



