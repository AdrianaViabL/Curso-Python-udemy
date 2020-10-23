"""
gerenciadores de contexto sao para controle de alguma função como = abrir e fechr conexo com banco dae dados
"""
# with open('abc.txt', 'w')as arquivo:
#     arquivo.write('alguma coisa')
#
#
# class Arquivo:
#     def __init__(self, arquivo, modo):
#         print('abrindo o arquivo')
#         self.arquivo = open(arquivo, modo)
#
#     def __enter__(self):
#         print('retornando arquivo')
#         self.arquivo.close()
#
#     def __exit__(self, exc_type, exc_val, exc_tb):  #onde serao tratados as excessoes
#         print('fechando o arquivo')
#         self, arquivo.close()
#         #depois de ter tratado a excessao
#         return True
#
# with Arquivo('abc.txt', 'w')as arquivo:
#     arquivo.qualquercoisa('alguma coisa')

from contextlib import contextmanager


@contextmanager
def abrir(arquivo, modo):
    try:
        print('Abrindo o arquivo')
        arquivo = open(arquivo, modo)
        yield arquivo
    finally:
        print('fechando o arquivo')
        arquivo.close()


with abrir('abc.txt', 'w') as arquivo:  #deve ser usado com with para que seja executado aabertura/fechamento do arquivo
    arquivo.write('Linha 1 \n')
    arquivo.write('Linha 2 \n')
    arquivo.write('Linha 3 \n')
