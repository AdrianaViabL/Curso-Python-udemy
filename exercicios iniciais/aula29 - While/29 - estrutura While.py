"""
while em Python
Realiza ações enquanto a condição for verdadeira
"""
x = 0

while x < 100:
    x += 1
    print(x)
print('Acabou o loop \o')
print(10 * '==')
print('Mostrando so os numeros pares')

x = 0
while x < 50:
    x += 1
    if x % 2 == 0:
        print(x)
    else:
        continue  # Ele nao executa o que está depois do continue

print(10 * '==')

print('mexendo com coluna e linha')
x = 0
while x <= 10:
    y = 0
    while y < 5:
        print(f'x{x}, y{y}')
        y += 1
    x += 1

print(10 * '==')
print('calculadora')

while True:
    num_1 = input('DIgite um numero: ')
    num_2 = input('DIgite outro numero: ')
    operador = input('digite um operador: ')
    sair = input('deseja sair? [s] ou [n]: ')

    if sair == 's':
        break

    if not num_1.isnumeric() or not num_2.isnumeric():
        print('digite um número válido')
        continue

    num_1 = int(num_1)
    num_2 = int(num_2)
    if operador == '+':
        print(f'{num_1} + { num_2} = {num_1 + num_2}')
    elif operador == '-':
        print(f'{num_1} - { num_2} = {num_1 - num_2}')
    elif operador == '*':
        print(f'{num_1} * { num_2} = {num_1 * num_2}')
    elif operador == '/':
        print(f'{num_1} / { num_2} = {num_1 / num_2}')
    else:
        print('digite um operador válido')

