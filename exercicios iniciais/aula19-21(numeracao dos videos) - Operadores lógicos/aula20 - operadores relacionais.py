"""
Operadores relacionais
== > >= < <= !=
"""

print(2 == '2')

idade1 = int(input('digite a primeira idade: '))
idade2 = int(input('digite a segunda idade: '))

if idade1 > idade2:
    print(f'a maior idade é {idade1}')
elif idade2 > idade1:
    print(f'a maior idade é {idade2}')
else:
    print(f'as duas idades são iguais')
