'''
artg e kwargs
'''

def func(*args, **kwargs):
    print(args)
    print(args[0])
    print(args[-1])  #mostra o ultimo item da tupla
    print(len(args))  #quanto itens tem na tupla
    idade = kwargs.get('idade')
    print(idade)


lista = [1, 2, 3, 4, 5, 6]
n1, n2, *n = lista
print(n1, n2, n)
print(10 * '===')
func(*lista)  # desmpacotando a lista para que os valores sejam atribuido em um indice da tupla
print(10 * '===')
func(lista)  #uma lista dentro de uma tupla

func(*lista, nome='Adriana', idade=26)
