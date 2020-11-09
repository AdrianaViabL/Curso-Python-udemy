class CarrinhoCompra:
    def __init__(self):
        self.produtos = []

    def inserir_prod(self, prod):
        self.produtos.append(prod)

    def lista_prod(self):
        for produto in self.produtos:
            print(produto.nome, produto.valor)

    def soma_total(self):
        total = 0
        for produto in self.produtos:
            total += produto.valor
        return total


class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor
