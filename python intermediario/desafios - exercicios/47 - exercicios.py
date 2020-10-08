'''
1 - crie uma função que exibe uma saudação com os parametros saudação e nome

2 - crie uma funçao que recebe 3 numeros com parametros e exiba a soma entre eles

3 - crie uma função que receba 2 numeros. o primeiro é um valor, o segundo um percentual.
retorne o valor do primeiro numero somado do aumento do percentual informado

4 - Fizz Buzz - Se o parametro da função for divisivel por 2, retorne fizz, se for divisivel por 5 retornar buzz.
se o parametro da função for divisivel por 5 e por 3, retorne FIzzBuzz, caso contrário, retorne o numero enviado
'''

print('ex1.: crie uma função que exibe uma saudação com os parametros saudação e nome')
def saudacao(saud, nome):
    print(saud, nome)

saudacao('\nHello!', 'Adriana')

print(10 * '====')
print('ex2.: crie uma funçao que recebe 3 numeros com parametros e exiba a soma entre eles')
nu1 = int(input('digite um numero: '))
nu2 = int(input('digite segundo numero: '))
nu3 = int(input('digite terceiro numero: '))
def soma(n1, n2, n3):
    return n1 + n2 + n3

total = soma(nu1, nu2, nu3)

print('resultado da soma ', total)

print(10 * '====')
print('ex3.: aumentando o percentual de um valor')
val = int(input('digite um numero: '))
percent = int(input('digite o percentual a ser aumentado: '))
def calc_percent(vl, perc):
    perce = vl * (perc / 100)
    return perce + vl

valor = calc_percent(val, percent)

print(valor)

print(10 * '====')
print('ex4.: FizzBuzz')
numero = int(input('informe um numero: '))
def FizzBuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return 'FizzBuzz'
    if num % 3 == 0:
        return 'Fizz'
    if num % 5 == 0:
        return 'Buzz'
    return num

resultado = FizzBuzz(numero)

print(resultado)
