'''
objeto iteravel - variaveis que podem ter o seu valor
objeto iterador - disponibiliza o valor interno seguinte
 a cada chamada(como se fosse um for) e ele so pode ser
 iterado uma unica vez por execução
'''

def gera():
    for n in range(100):
        yield n

g = gera()

print(g)  # mostrando o endereco do gerador que foi criado na função gera()
print(next(g))

# for v in g:
#     print(v)
import sys

l1 = [x for x in range(10000)]
l2 = (x for x in range(10000))

print(sys.getsizeof(l1))
print(sys.getsizeof(l2))


