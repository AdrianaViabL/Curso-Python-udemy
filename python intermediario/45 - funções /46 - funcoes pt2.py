'''
funções (def) em Python - return
'''

def funcao(var):
    print(var)


variavel = funcao('valor que quero pt1')

print(variavel)   # ele nao tem um valor valido para ser exibido pois nao esta sendo retornado nada para a variável

if variavel:
    print(variavel)
else:
    print('nao ha o que exibir pt 1')

def valor(var2):
    return var2
    print('isso nao sera executado')

variavel = valor('valor a ser exibido')
if variavel:
    print(variavel)
else:
    print('nao ha o que exibir')

print(10 * '====')

def f(var):
    print(var)

def dumb():
    return f  #referenciando sem ter o uso de (), a função nao é executada, ele so passa a função para a variavel que esta sendo atribuida


valor = dumb()
print(valor, type(valor))

valor('\npode ser impresso algo na tela')

