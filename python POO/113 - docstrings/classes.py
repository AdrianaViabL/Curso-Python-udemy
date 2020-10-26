"""
Descrição rapida e simples

Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

"""

class MinhaClasse:
    """Documentacao normal

    conforme qualquer outra documentação
    """
    atributo1 = 1
    atributo2 = 'valor qualquer'
    def __init__(self, valor):
        """
        Inicializa valores
        :param valor:
        """
        self.valor = valor
        self.exibe_texto(valor)

    @staticmethod
    def exibe_texto(texto):
        """
        metodo que exibe 100 caracteres na tela
        :param texto:
        :return:
        :raise Value error
        """
        if not isinstance(texto, str):
            raise TypeError('texto precisa ser uma string')

        if len(texto) >= 100:
            raise ValueError('texto precisa ter 100 caracteres ou menos')
        return texto
