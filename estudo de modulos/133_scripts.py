#!/usr/bin/env python3
import sys
import os
#para executar(no linux) coloque python3 no terminal  + nome arquivo .py
argumentos = sys.argv
print(argumentos)
qtd_argumentos = len(argumentos)
if qtd_argumentos <= 1:
    print('Faltando argumentos:')
    print('-a', 'para listar todos os arquivos nesta pasta', sep='\t')
    print('-d', 'para listar todos os diretorios nesta pasta', sep='\t')
    sys.exit()

so_arquivos = False
so_diretorios = False
if '-a' in argumentos:
    so_arquivos = True
if '-d' in argumentos:
    so_diretorios = True

for arquivo in os.listdir('.'):
    if so_arquivos:
        if os.path.isfile(arquivo):
            print(arquivo)

    if so_diretorios:
        if os.path.isdir(arquivo):
            print(arquivo)