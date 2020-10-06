"""
while / Else
contadores
acumuladores
"""
contador = 1
acumulador = 1

while contador <= 20:
    print(contador, acumulador)
    acumulador += contador
    contador += 1
    if contador > 7:
        break
else:
    print('cheguei no else')

print('sai do while')
