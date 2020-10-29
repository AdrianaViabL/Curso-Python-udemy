"""
usando o iterator para refazer uma lista(exeplo de como funciona por 'debaixo dos panos')
"""


class MinhaLista:
    def __init__(self):
        self.__itens = []
        self.__index = 0

    def add(self, valor):
        self.__itens.append(valor)

    def __iter__(self):  # serviria para se caso outra classe fosse responsavel por iteragir com essa classe
        return self

    def __getitem__(self, index):  # para que os valores possam ser acessados via indice[0],
        return self.__itens[index]

    def __setitem__(self, index, valor):  # permite que o valor dentro da lista seja alterado
        if index >= len(self.__itens):  # validando se o indice informado existe na lista
            self.__itens.append(valor)

        self.__itens[index] = valor

    def __delitem__(self, index):
        del self.__itens[index]

    def __next__(self):
        try:
            item = self.__itens[self.__index]
            self.__index += 1
            return item
        except IndexError:
            raise StopIteration  # fazendo com que ele nao de erro quando a lista for usada em um FOR

    def __str__(self):
        return f'{self.__class__.__name__}({self.__itens})'


if __name__ == "__main__":
    lista = MinhaLista()
    lista.add('Adriana')
    lista.add(123456)
    lista.add('qualquer coisa')
    print(lista)

    for valor in lista:
        print(valor)

    lista.add('valor qualquer')
    print(lista)
    del lista[3]  # conseguindo apagar itens da lista
    print(lista)
