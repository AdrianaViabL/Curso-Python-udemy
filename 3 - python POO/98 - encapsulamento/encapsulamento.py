"""
public, protected e private - formas de declaração de
variaveis dentro do POO(para a maioria das linguagens)
forma por convenção de ser declarado variaveis com limitação de acesso
_ - proximo de um protected
__ - private

quando uma variavel ou método é criada com o _ antes do seu nome, ela
NÃO DEVE SER ALTERADA FORA DA CLASSE
"""


class BaseDados:
    def __init__(self):
        self.__dados = {}
    @property
    def dados(self):
        return self.__dados

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})

    def lista_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)

    def apaga_cliente(self, id):
        del self.__dados['clientes'][id]


base = BaseDados()
base.inserir_cliente(1, 'Adriana')
base.inserir_cliente(2, 'João')
base.inserir_cliente(3, 'Maria')
base.lista_clientes()
base.apaga_cliente(2)
print('apos excluir um cliente\n')
base.lista_clientes()
print(10 * '========')

bd = BaseDados()
bd.inserir_cliente(1, 'xxxxx')
bd.inserir_cliente(2, 'yyyyy')
bd.__dados = 'um outro valor'
print(bd._BaseDados__dados)
print(bd.__dados)
print(bd.dados)  #acessando atraves da função GET
bd.dados = 'qualquer coisa'  # vai dar erro pois nao existe uma função para atribuir valor para essa variavel
