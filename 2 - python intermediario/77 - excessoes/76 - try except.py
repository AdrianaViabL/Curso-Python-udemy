"""
Tratamento de execoes
"""

try:
    a = {}
    print(a)
except NameError as erro:
    print('deu ruim \n', erro)
except (IndexError, KeyError) as erro:
    print('erro de indice ou chave', erro)
except Exception as erro:
    print('ocorreu um erro inesperado ', erro)
else:
    pass
finally:
    print('vai passar de qualquer jeito por aqui')

print('depois de passar pelas excessoes')

print(a)