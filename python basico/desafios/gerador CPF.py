from random import randint

cpf_novo = str(randint(100000000, 999999999))
dig1 = dig2 = 0
print(cpf_novo)
valor = 0
for i, v in enumerate(range(10, 1, -1)):
    num = int(cpf_novo[i])
    print(num)
    valor += num * v

if 11 - valor % 11 >= 9:
    dig1 = 0
else:
    dig1 = 11 - valor % 11

valor = 0
for i, v in enumerate(range(11, 1, -1)):
    num = int(cpf_novo[i])
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

