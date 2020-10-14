"""
1 - crie uma função1 que recebe uma função2 como parametro e retorne o valor da função2 executada

2 - crie uma função1 que recebe uma função2 como parametro e retorne o valor da função2 executada.
faça a função1 executar duas funções que recebam um numero diferente de argumentos
"""

print('ex1.:trabalhando com duas funções')
#
def func2():
    return 'Passou por aqui'

def func1(funcao):
    return funcao()

executado = func1(func2)
print(executado)
print(type(executado))

print('ex2.:trabalhando com tres funções')

def mestre(func, *args, **kwargs):
    return func(*args, **kwargs)

def fala_oi(nome):
    return f'Oi {nome}'

def saudacao(nome, saudacao):
    return f'{saudacao} {nome}'

executado = mestre(fala_oi, 'Adriana')

print(executado)

executando2 = mestre(saudacao, 'Adriana', saudacao='Bom dia')

print(executando2)