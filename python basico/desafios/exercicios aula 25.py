"""
Faça um programa que peça ao usuário para digitar um numero inteiro,
informe se esse numero é par ou ímpar. Caso o usuário nao digite um
número, informe que não é um núpero
"""
print('Exercicio 1 - par ou ímpar\n')

num = input('digite um numero inteiro: ')
if num.isdigit():
    num = int(num)
    if num % 2 == 0:
        print(f'O número {num} é par!')
    else:
        print(f'O número {num} é impar!')
else:
    print('valor digitado inválido')
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no
horário descrito, exiba a saudação apropriada. bom dia 0-11, 
boa tarde 12-17 e boa noite 18-23
"""
print(10 *'===')
print('Exercício 2 - horas do dia\n')
hora = input('digite um horário(de 00 ate 23): ')
if hora.isdigit():
    hora = int(hora)

    if 0 < hora <= 11:
        print('bom dia')
    elif hora < 18:
        print('Boa tarde')
    elif hora <= 23:
        print('boa noite')
    else:
        print('Digite uma hora válida')
else:
    print('Digite uma hora válida')

"""
faça um programa que peça o primeiro nome do usuário. Se o nome
tiver 4 letras ou menos escreva "Seu nome é curto"; se tiver entre
5 e 6 letras "Seu nome é normal"; maior que 6 "Seu nome é muito grande"
"""
print(10 *'===')
print('Exercício 3 - quantidade de letras em um nome\n')

nome = input('Digite o seu primeiro nome: ')
tamanho = len(nome)
if tamanho <= 4:
    print('Seu nome é curto')
elif tamanho <= 6:
    print('Seu nome é normal')
else:
    print('Seu nome é muito grande')
