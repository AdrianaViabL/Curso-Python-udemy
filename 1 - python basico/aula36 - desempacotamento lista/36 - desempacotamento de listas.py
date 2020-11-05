"""
Desempacotamento de listas em Python
o valor de uma lista sera atribuido a varias variaveis
"""
lista = ['Luiz', 'João', 'Maria', 1, 2, 3, 100]
print(f'lista completa {lista}')
n1, n2, *outro_valor, untimo_val_lista = lista
print(n1, n2)
print(outro_valor)
print(untimo_val_lista)


