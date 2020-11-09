l1 = [1, 2, 3, 4, 5, 6, 7]
ex1 = [val for val in l1]
print('passando valor a valor para a variavel ex1 \n', ex1)

ex2 = [v * 2 for v in l1]

print('multiplicando usando compreensao de lista \n', ex2)

ex3 = [(v, v2) for v in l1 for v2 in range(3)]

print(ex3)

l2 = ['Adriana', 'Luiz', 'Mauro']
ex4 = [v.replace('a', '@').upper() for v in l2]

print(ex4)

tupla = (
    ('chave', 'valor'),
    ('chave2', 'valor2')
)

ex5 = [(y, x) for x, y in tupla]
print('invertendo os valores da tupla \n', ex5)

l3 = list(range(100))

ex6 = [v for v in l3 if v % 2 == 0 if v % 8 == 0] # pegando so os numeros pares e divisiveis por 8

print(ex6)

ex7 = [v if v % 3 == 0 else 0 for v in l3]

print(ex7)