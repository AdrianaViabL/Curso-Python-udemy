"""
Operadores aritméticos
+, -, *, /, //(divisao inteira), **, %(resto divisao), ()
"""
val1 = 10
val2 = 3

print(f'soma de {val1} {val2} = ', val1 + val2)  # soma

print(f'subtração de {val1} {val2} = ', val1 - val2)  # subtração
print(f'divisão de {val1} {val2} = ', val1 / val2)  # divisão
print(f'div. inteira de {val1} {val2} = ', val1 // val2)  # div. inteira
print(f'exponenciação de {val1} {val2} = ', val1 ** val2)  # exponenciação
print(f'resto divisao de {val1} {val2} = ', val1 % val2)  # resto divisao
print(f'usando parenteses ({val1} + {val2}) * 2 = ', (val1 + val2) * 2)
print(2 + 5 * 3 ** 2 - (23.5 + 23.5))
