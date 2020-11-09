"""
Pilhas e filas
Pilha (stack) - LIFO - last in, first out.
Ex.: pilha de livros que sao adicionados um sobre o outro
fila (queue) - FIFO - first in, first out
Ex.: uma fila de banco
Filas podem ter efeitos colaterais em desempenho, porque a cada item
alterado, todos os indices serão modificados
"""

livros = list()
livros.append('Livro 1')
livros.append('Livro 2')
livros.append('Livro 3')
livros.append('Livro 4')
livros.append('Livro 5')
livro_removido = livros.pop()
print(livro_removido)
print('\nFilas\n')
from collections import deque

fila = deque()  # ele pode ser iterado igual uma lista
fila.append('Joaozinho')
fila.append('Maria')
fila.append('Luiz')
fila.append('MArcos')
fila.append('Jose')

print(f'saiu: {fila.popleft()}')
for nome in fila:
    print(nome)

print(10 * "=====")

fila2 = deque(maxlen=5)
fila2.extend([1, 2, 3, 4])
fila2.append(5)
fila2.append(6)  # o elemento mais antigo da lista é removido da fila

print(fila2)
fila.insert(4, 'Luiz')
print(fila)

print(10 * "=====")

Fila3 = deque()
Fila3.extend([10, 20, 30, 40, 50, 60, 70, 80])
print(Fila3.index(30))  # achando o indice do valor na lista
Fila3.reverse()
print(Fila3)
Fila3.rotate(2)
print(Fila3)