'''
split, join e enumerate em python
split - divide uma string
join - juntar uma lista
enumerate - enumera elementos da lista
'''

string = 'texto de , exemplo de frase'
lista1 = string.split(' ')
lista2 = string.split(',')
print(string)
print(lista1)  #texto tendo sido transformado em uma lista
print(lista2, '\n')

palavra = ''
contagem = 0
print('vendo qual palavra se repete mais vezes na lista ', lista1)
for valor in lista1:
    qtd_vezes = lista1.count(valor)
    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor

print(f'A palavra que apareceu mais vezes é {palavra} ({contagem}x)')
print(10 * '----', '\n')
print('usando a funcao split - retirando espaços no inicio e final de uma string')

frase_espaco = '    uma frase com espaco no inicio e no final    '
print(frase_espaco)
print(frase_espaco.strip().capitalize())

print(10 * '----', '\n')
print('juntando elementos de uma lista com o JOIN')
string2 = 'o Brasil é penta.'
lista = string2.split(' ')
string3 = ' '.join(lista)

print(string2)
print(lista)
print(string3)

print(10 * '----', '\n')
print('usando o Enumerate, usado mais com manipulaçao de tuplas')
for indice, valor in enumerate(lista):
    print(indice, valor, lista[indice])  # duas formas de fazer a mesma coisa



print(10 * '----', '\n')
cadastro = [
    [1, 'Luiz'],
    [2, 'Maria'],
    [3, 'Joao']]
print('uma lista dentro de outra lista ', cadastro)
for indice, nome in cadastro:
    print(indice, nome)

print(10 * '----', '\n')
nomes = ['luiz', 'maria', 'joao']
print(f'acrescentando indice em uma lista com o Enumerate {nomes}')

for indice, nome in enumerate(nomes):
    print(indice, nome)

