import re

regressivo = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]


def valida(cnpj):
    cnpj = numeros(cnpj)
    if not cnpj.isnumeric():
        print('somente valores numericos!!!')
        return False

    if len(cnpj) < 12:
        print('tamanho de cnpj invalido')
        return False

    if valida_sequencia(cnpj):  # caso seja uma sequencia de numeros iguais
        return False

    cnpj_comd1 = valida_d1(cnpj)
    novo_cnpj = valida_d2(cnpj_comd1)
    if novo_cnpj == cnpj:
        return True
    else:
        return False


def valida_sequencia(cnpj):
    sequencia = cnpj[0] * len(cnpj)
    if sequencia == cnpj:
        print('valor invalido!! Não podem ser numeros iguais!!!')
        return True
    else:
        return False


def numeros(cnpj):
    return re.sub('[^0-9]', '', cnpj)


def valida_d1(cnpj):
    regressivos = regressivo[1:]
    novo_cnpj = cnpj[:-2]
    total = 0
    for i, regres in enumerate(regressivos):
        total += int(cnpj[i]) * regres

    d1 = 11 - total % 11
    if d1 > 10:
        d1 = 0
    return f'{novo_cnpj}{d1}'


def valida_d2(cnpj):
    total = 0
    novo_cnpj = cnpj
    for i, regres in enumerate(regressivo):
        total += int(cnpj[i]) * regres

    d2 = 11 - total % 11
    if d2 >= 9:
        d2 = 0
    return f'{cnpj}{d2}'
