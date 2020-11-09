import re


def valida_cpf(cpf):
    cpf = str(cpf)
    cpf = re.sub('[^0-9]', '', cpf)
    cpf_novo = list(cpf[:-2])
    if len(cpf) != 11 or isinstance(cpf, int):
        print('digite um CPF válido!!!!')
    else:
        valor = 0
        for i, v in enumerate(range(10, 1, -1)):
            num = int(cpf_novo[i])
            valor += num * v
            if v == 2:
                break

        if 11 - valor % 11 > 9:
            dig1 = 0
        else:
            dig1 = 11 - valor % 11

        valor = 0
        cpf_novo.append(str(dig1))

        for i, v in enumerate(range(11, 1, -1)):
            num = int(cpf_novo[i])
            valor += num * v

        if 11 - valor % 11 > 9:
            dig2 = 0
        else:
            dig2 = 11 - valor % 11

        cpf_novo.append(str(dig2))
        cpf_novo = ''.join(cpf_novo)
        if cpf == cpf_novo:
            return True  # valido
        else:
            return False  # invalido
