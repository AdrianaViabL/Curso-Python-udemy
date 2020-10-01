nome = 'Adriana'
idade = 26
altura = 1.70
peso = 80

imc = peso/ (altura ** 2)
print(f'{nome} tem {idade} anos de idade e seu IMC é {imc:.2f}')

print('outra forma de formatar uma frase ')

print('{} tem {} anos de idade e seu IMC é {}'.format(nome, idade, imc))
print('{n} tem {i} anos de idade e seu IMC é {im}'.format(n=nome, i=idade, im=imc))  # renomeando as variáveis
