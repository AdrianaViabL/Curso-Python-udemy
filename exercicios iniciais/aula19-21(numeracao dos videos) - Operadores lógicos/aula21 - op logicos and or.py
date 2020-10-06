#Operadores logicos and, or, not in

a = 10
b = 30
c = 14

if a < b and not c < a:
    print('verdadeiro')
else:
    print('falso')

print(14 * '--')
if b < c or c > a:
    print('um dos casos foi verdadeiro')
else:
    print('nenhum dos casos foi verdadeiro')