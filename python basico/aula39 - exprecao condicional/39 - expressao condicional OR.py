nome = input('Qual seu nome?: ')
print(nome or None or False or 0 or 'voce nao digitou nada')

print(10 * '====')

a = 0
b = None
c = False
d = []
e = {}
f = 22
g = 'nome'

variavel = a or b or c or d or e or f or g
print(variavel)  # ele vai atribuir o primeiro valor que for verdadeiro
