'''
pegue o preco dos produto e some usando compreeção de lista
'''

carrinho = []

carrinho.append(('Produto 1', 40))
carrinho.append(('Produto 2', 10))
carrinho.append(('Produto 3', 50))
carrinho.append(('Produto 4', 20))
carrinho.append(('Produto 5', 10))


valor = sum([float(val) for prod, val in carrinho])
print(valor)
