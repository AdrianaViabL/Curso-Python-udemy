#contando a quantidade de caracteres em uma string(nao funciona em int e float)
frase = input('digite uma frase: ')
qtdTexto = len(frase)

if qtdTexto < 9:
    print('digite uma frase com mais de 9 caracteres')
else:
    print('a frase tem mais de 9 caracteres')

print(10 * '===')

string1 = input('Digite qualquer coisa: ')
string2 = input('Digite outra coisa: ')

print(f'A quantidade de caracteres digitados foi {len(string1) + len(string2)}')
print(10 * '===')
print('usando funções de validação\n')
val1 = input('digite um numero ')
val2 = input('digite outro numero ')

if val1.isnumeric() and val2.isnumeric():
    val1 = int(val1)
    val2 = int(val2)
    print(f'os valores digitados são numéricos, somados dao: {val1 + val2}')
else:
    print('um dos valores não é numérico')
try:  #vai tentar executar, caso de erro ele executa o except
    val1 = int(val1)
    val2 = int(val2)
    print(f'os valores digitados são numéricos, somados dao: {val1 + val2}')
except:
    print('um dos valores não é numérico')