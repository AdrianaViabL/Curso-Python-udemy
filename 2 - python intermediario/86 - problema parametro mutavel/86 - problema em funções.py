def lista_de_cliente(cliente_iter, lista=None):  # 'lista=[]' uma lista mutavel dentro de uma função pode gerar comportamentos bizarros
    if lista is None:
        lista = []
    lista.extend(cliente_iter)
    return lista

print('para ver o comportamento bizarro acontecendo, substitua lista=None por lista=[]')
lista_cliente1 = ['Fabricio']
cliente1 = lista_de_cliente(['João', 'Maria', 'Eduardo'], lista_cliente1)
cliente2 = lista_de_cliente(['Marcos', 'Jonas', 'Zico'])
cliente3 = lista_de_cliente(['José'])

print(cliente1)
print(cliente2)
