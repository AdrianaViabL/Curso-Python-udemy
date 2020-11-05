import math

PI = math.pi

def dobra_lista(lista):
    return [x*2 for x in lista]

def multiplica(val):
    r = 1
    for i in val:
        r *= i
    return r

if __name__ == '__main__':  #fazendo com que essa area final nao seja executada quando o calculos.py for chamado por outro modulo
    print(PI)
    print(__name__)


