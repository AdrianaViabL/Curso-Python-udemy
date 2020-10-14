lista = [
    ['P1', 13],
    ['P2', 4],
    ['P3', 10],
    ['P4', 50],
    ['P5', 30]
]

print('usando o lambda para ordenar a lista, sem '
      'precisar criar uma função para se indicar \n'
      'por onde a lista deve ser ordenada')

print('lista sorteada = ', sorted(lista, key=lambda i: i[1]))

print('lista orginal = ', lista)
