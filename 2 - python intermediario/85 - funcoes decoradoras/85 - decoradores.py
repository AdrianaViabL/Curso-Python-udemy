"""
funções decoradas e decoradores
decorador - @master - que recebem outra função para ser executada
decorada -  estão sendo executadas atraves de outras funções, sendo enviadas como parametro de execução
"""
def master(funcao):
    def slave(*args, **kwargs):
        print('agora estou decorada')
        funcao(*args, **kwargs)  # *args, **kwargs - colocados para que a função escrava possa aceitar parametros
    return slave  #retornando a função sem executá-la transformando a variavel que recebe ela em uma função

@master
def fala_oi():
    print('Oi')

def recebe_oi(oi):
    print(oi)

print('usando a função diretamente')
recebe_oi('ola mundo')
print(10 * '=====')

print('unsando a função atraves de um decorador')
@master
def recebe_args(oi):
    print(oi)

recebe_args('estou dentro de um decorador \o/')


print(10 * '=====')

from time import sleep, time

def velocidade(funcao):
    def interna(*args, **kwargs):
        start_time = time()
        resultado = funcao(*args, **kwargs)
        end_time = time()
        tempo = (end_time - start_time) * 1000
        print(f'A função {funcao.__name__} demorou {tempo:.2f}ms para executar')
        return resultado
    return interna

@velocidade
def demora():
    for i in range(5):
        print(i)
        sleep(1)

demora()
