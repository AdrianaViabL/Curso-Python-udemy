"""
ex.: usando o try para tratar de situações de conversão de valores
"""

def converter_numero(val):
    try:
        val = int(val)
        return val
    except ValueError:
        try:
            val = float(val)
            return val
        except ValueError:
            pass

print('digite 0 para sair do loop')
while True:
    numero = input('digite um valor: ')
    val_novo = converter_numero(numero)
    if val_novo is not None:
        if val_novo == 0:
            break
        print(val_novo * 2)
    else:
        print('digite apenas numeros!!!')

