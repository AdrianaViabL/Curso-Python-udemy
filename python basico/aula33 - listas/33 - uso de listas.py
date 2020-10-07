"""
Listas em Python
fatiamento
append, insert, pop, del clear, extend,
min, max
range
"""
# indice  0    1    2    3    4
lista = ['A', 'B', 'C', 'D', 10.5]
# neg -   5    4    3    2    1

print(lista)
print(10 * '----')
print('concatenando listas')
l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = l1 + l2

print(f'lista 1 = {l1}')
print(f'lista 2 = {l2}')
print(f'lista 1 e 2 concatenadas com o sinal de + =  {l3}')
print('ou usando o Extend para acrescentar algo em uma lista')
l1.extend(l2)

print(f'lista 1 e 2 juntas na lista 1 = {l1}')
print(10 * '----')
print('eliminando o item final da lista usando "pop"')

l1.pop()
print(f'lista 1 {l1}')
print(10 * '----')
print('usando o del para excluir os itens da lista')
print(f'lista l1 sem os itens do index 2 ate 4')
del(l1[2:4])

print(f'lista 1 {l1}')

print(f'mostrando o maior valor da lista 1 = {max(l1)}')
print(f'mostrando o menor valor da lista 1 = {min(l1)}')

print(10 * '----')
print('verificando o tipo de valor dentro de uma lista')
l1 = ['string', True, 10, -10.5]

for elem in l1:
    print(f'o tipo de "{elem}" é {type(elem)}')

print(10 * '----')
print('brincando de forca')

secreto = 'perfume'
digitadas = []
chances = 3

while True:
    if chances <= 0:
        print('')
    letra = input('Digite uma letra: ').lower()
    if len(letra) > 1:
        print('Ahhh, isso nao vale, digite apenas uma letra.')
        continue
    digitadas.append(letra)

    if letra in secreto:
        print(f'Parabéns, a letra {letra} existe na palavra secreta')
    else:
        print(f'Pena :(, a letra digitada nao existe')
        digitadas.pop()
        print(f'voce tem ainda {chances} para descobrir a palavra secreta')
        chances -= 1

    secreto_temp = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temp += letra_secreta
        else:
            secreto_temp += '*'

    if secreto_temp == secreto:
        print(f'Que legal, você ganhou!!! A palavra era "{secreto_temp}".')
        break
    else:
        print(f'a palavra secreta até agora = {secreto_temp}')


