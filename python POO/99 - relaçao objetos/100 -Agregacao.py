from clAgrega import CarrinhoCompra, Produto

carrinho = CarrinhoCompra()

p1 = Produto('camiseta', 50)
p2 = Produto('tenis', 150)
p3 = Produto('celular', 2500)

carrinho.inserir_prod(p1)
carrinho.inserir_prod(p2)
carrinho.inserir_prod(p3)
carrinho.lista_prod()

print(carrinho.soma_total())
