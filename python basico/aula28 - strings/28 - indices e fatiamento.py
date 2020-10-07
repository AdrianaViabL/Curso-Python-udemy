"""
Manipulando strings
* String indice
* Fatiamento de strings
* Funções build-in len, abs, type, print, etc...
Essas funções podem ser usadas diretamente em cada tipo
"""
#ind positivo  {012345678}
texto       =  'python s2'
#ind negativo -{987654321}
print(texto[2]) #acessando o valor dentro da variável por índice
url = 'www.google.com.br/'
print(f'mostrando sem o ultimo caractere {url[:-1]}')
print('fatiando uma string')

print(texto[:6])
print(texto[2:6])
print(texto[7:])

print('usando indice negativo')
print(texto[:-6])
print(texto[-3:-9])
print(texto[-4:])

print('pulando caracteres')
print(f'pulando duas letras: {texto} = {texto[0::2]}')

for letra in texto:
    print(letra)
