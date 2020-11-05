'''
um contador indo pela contagem regressiva e outro tendo incremento a cada passagem pelo loop
'''

contrario = 10
for var in range(0, 9):
    print(var, contrario)
    contrario -= 1

print('\nresolução do professor')

for i, r in enumerate(range(10, 1, -1)):
    print(i, r)
