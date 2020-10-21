"""
trbalhando com atributos de classes(ou variaveis)
a partir do momento que se tem uma variavel global,
o valor dela pode ser acessado tanto por instancia da
classe como diretamente pela classe, mas o seu valor so
vai ser editado em uma instancia a partir do momento que
 for atribuido diretamente valor a ela
"""


class A:
    val = 123

    def __init__(self):  #valor que sera atribuido as instancias, mas o valor 'original' continua sendo o de raiz
        self.val = 321


a1 = A()
a2 = A()

a1.val = 456  # alterando o valor dentro da instancia da classe a1
print(a1.val)
print(a2.val)
print(A.val)
