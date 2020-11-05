from dados import produtos, pessoas, qualquercoisa
# forma usando a função map()
# nov_list = map(lambda x:x * 2, qualquercoisa) #multiplicando os valores da nova lista
# print(nov_list)
# print(list(nov_list))
#
# print('forma usando o list comprehesion')
# lista_compreendida = [x * 2 for x in qualquercoisa]
# print(lista_compreendida)

def aumenta_preco(p):
    p['preco'] = round(p['preco'] * 1.05, 2)
    return p

precos = map(lambda p: p['preco'], produtos)   #acessando a coluna de preco

novo_preco = map(aumenta_preco, produtos)

print(list(novo_preco))
print('usando a lista de nomes, alterando as idades \n')

#nomes = map(lambda p:p['nome'], pessoas)  #pegando os nomes das pessoas
def aumenta_idade(p):
    p['nova_idade'] = round(p['idade'] * 1.20)
    return p

nomes = map(aumenta_idade, pessoas)

for n in nomes:
    print(n)