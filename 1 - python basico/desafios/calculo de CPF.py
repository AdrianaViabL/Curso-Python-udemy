import re
cpf = input('digite o seu CPF: ')

cpf = re.sub('[^0-9]', '', cpf)
cpf_novo = []
dig1 = dig2 = 0
if len(cpf) < 11:
    print('digite um CPF válido!!!!')
else:
    valor = 0
    for i, v in enumerate(range(10, 1, -1)):
        num = int(cpf[i])
        cpf_novo.append(cpf[i])  #com certeza 'novo_cpf = cpf[:-2]' é mais simples
        valor += num * v

    if 11 - valor % 11 >= 9:
        dig1 = 0
    else:
        dig1 = 11 - valor % 11

    valor = 0
    for i, v in enumerate(range(11, 1, -1)):
        num = int(cpf[i])
        valor += num * v
        if v == 2:
            valor += dig1 * v

    if 11 - valor % 11 >= 9:
        dig2 = 0
    else:
        dig2 = 11 - valor % 11

    cpf_novo.append(str(dig1))
    cpf_novo.append(str(dig2))
    cpf_novo = ''.join(cpf_novo)
    print(cpf_novo)
    if cpf == cpf_novo:
        print(f'CPF {cpf} é valido')
    else:
        print(f'CPF {cpf} NÃO é valido')

print(10 * '=====')
print('resolução do professor')

while True:
    # cpf = '16899535009'
    cpf = input('Digite um CPF: ')
    novo_cpf = cpf[:-2]                 # Elimina os dois últimos digitos do CPF
    reverso = 10                        # Contador reverso
    total = 0

    # Loop do CPF
    for index in range(19):
        if index > 8:                   # Primeiro índice vai de 0 a 9,
            index -= 9                  # São os 9 primeiros digitos do CPF

        total += int(novo_cpf[index]) * reverso  # Valor total da multiplicação

        reverso -= 1                    # Decrementa o contador reverso
        if reverso < 2:
            reverso = 11
            d = 11 - (total % 11)

            if d > 9:                   # Se o digito for > que 9 o valor é 0
                d = 0
            total = 0                   # Zera o total
            novo_cpf += str(d)          # Concatena o digito gerado no novo cpf

    # Evita sequencias. Ex.: 11111111111, 00000000000...
    sequencia = novo_cpf == str(novo_cpf[0]) * len(cpf)

    # Descobri que sequências avaliavam como verdadeiro, então também
    # adicionei essa checagem aqui
    if cpf == novo_cpf and not sequencia:
        print('Válido')
    else:
        print('Inválido')