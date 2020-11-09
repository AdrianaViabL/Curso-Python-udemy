frase = 'o rato roeu a roupa do rei de roma'
tam_frase = len(frase)
contador = 0
while contador < tam_frase:  #exibindo o texto uma letra abaixo da outra
    print(frase[contador])
    contador += 1

print(10 * '----')
nova_string = ''  #declarando uma variável vazia
contador = 0
while contador < tam_frase:
    letra = frase[contador]
    if frase[contador] == 'r':
        nova_string += 'R'
    else:
        nova_string += letra
    print(nova_string)
    contador += 1

