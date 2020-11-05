"""
Formatando valores com modificadores

:s - texto (strings)
:d - inteiros (int)
:f - números de pontos flutuantes (float)
:.(numero)f -  quantidade de casas decimais
:(caractere)(> ou < ou ^)(quantidade)(tipo - s, d ou f)

> - esquerda
< - direita
^ - centro
"""
num1 = 10
num2 = 3
divisao = num1 / num2
print('{:.2f}'.format(divisao))
val = 222  # funciona tanto para int como para strings
print(f'valor extra a esquerda {val:0>10}')
#faz com que o valor dentro da variável tenha um tamanho de 10 digitos
# contando com o que ja existe, jogando para a esquerda o que ja existe
print(f'valor extra a direita {val:0<10}')
print(f'valor extra centralizado {val:0^10}')
nome = 'Adriana sauro'
print(f'{nome:#^26}')

val1 = 'sardinha'
val2 = 'atum'
val_formatado = '{0:#^40} \n{1:%^40}'.format(val1, val2)
print(val_formatado)

print('mudando os caracteres dentro de uma string\n')

print(nome.lower())
print(nome.upper())
print(nome.title())
print(nome.capitalize())