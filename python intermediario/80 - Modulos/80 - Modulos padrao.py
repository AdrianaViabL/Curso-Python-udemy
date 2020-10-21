"""
Módulos padrao do Python
Módulos sao arquivos .py e servem para expandir
as funcionalidades padraod da linguagem
https://docs.python.org/3/py-modindex.html
"""
import sys  # uso de modulos

print(sys.platform)  # ele mostra em qual sistema operacional o codigo esta rodando



from random import randint


def randint(*args):  # a partir dessa linha a função esta sendo alterada
    return 'sobreposição de função'


print(randint(0, 10))


