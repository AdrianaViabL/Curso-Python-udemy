from itertools import count

contador = count(start=1, step=2)

print(next(contador))
print(next(contador))
print(next(contador))
print(next(contador))
print(next(contador))
print(next(contador))
print(next(contador))
print('se for colocado dentro de um FOR, se tornara um LOOP INFINITO')
