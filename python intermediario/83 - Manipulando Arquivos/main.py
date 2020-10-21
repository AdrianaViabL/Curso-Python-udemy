#https://docs.python.org/3/library/functions.html#open

file = open('abc.txt', 'w+')
file.write('linha 1\n')
file.write('linha 2\n')
file.write('linha 3\n')
file.seek(0, 0)  #voltando ate o inicio do arquivo para ler os dados

print('lendo linhas')
print(file.read())

print(10 * '=====')

file.seek(0, 0)  #voltando ate o inicio do arquivo para ler os dados
print(file.readline(), end='')  # fazendo com que nao tenha ular linha

print(10 * '=====')

file.seek(0, 0)  #voltando ate o inicio do arquivo para ler os dados
print(file.readlines())  #o \n so some se for usado um for para mostrar os dados
file.close()

print(10 * '=====')
print('outra forma de lidar com arquivos, mas nao sendo "pytonico"')
try:
    file2 = open('teste2.txt', 'w+')
    file2.write('linha de teste')
    file2.seek(0, 0)
    print(file2.read())
finally:
    file2.close()

print(10 * '=====')
print('forma pytonica de acessar arquivos')

with open('abc.txt', 'w+') as file:  # o with ja vai fechar o arquivo no final da execução
    file.write('linha 1\n')
    file.write('linha 2\n')
    file.write('linha 3\n')

    file.seek(0)
    print(file.read())

apagar = open('vaiserapagado.txt', 'a+')
apagar.write('valor adicionado')
apagar.write('valor adicionado2')

import os
os.remove('vaiserapagado.txt')



