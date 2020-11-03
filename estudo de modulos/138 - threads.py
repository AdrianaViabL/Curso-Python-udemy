"""
executando varios processos ao mesmo tempo
"""
from threading import Thread, Lock
from time import sleep


class MeuThread(Thread):
    def __init__(self, texto, tempo):
        self.texto = texto
        self.tempo = tempo
        super().__init__()

    def run(self):
        sleep(self.tempo)
        print(self.texto)


# t1 = MeuThread('Thread 1', 2)
# t1.start()
#
# t2 = MeuThread('Thread 2', 3)
# t2.start()
#
# t3 = MeuThread('Thread 3', 5)
# t3.start()
#
# for i in range(20):
#     print(i)
#     sleep(1)

print(10 * '====')
print('outra forma de trabalhar com Threads')


def vai_demorar(texto, tempo):
    sleep(tempo)
    print(texto)


t = Thread(target=vai_demorar, args=('Olá mundo', 5))


# t.start()
#  a execução finaliza no meio do FOR
# for i in range(20):
#     print(i)
#     sleep(.5)

# while t.is_alive():
#     print('Esperando a Thread finalizar.')
#     sleep(2)

# th = Thread(target=vai_demorar, args=('Olá mundo', 10))
# th.start()
# # esse JOIN faz com que outros processos fiquem parados enquanto a Thread nao finalizar
# th.join()
# print('Thread acabou!')


class Ingresso:
    def __init__(self, estoque):
        self.estoque = estoque
        self.lock = Lock()

    def comprar(self, quantidade):
        self.lock.acquire()  # trancando a funcao por dentro, para nao ter varias entradas
        if self.estoque < quantidade:
            print('Não temos ingressos suficientes')
            self.lock.release()  # liberando para que a proxima execucao da instancia entre na funcao
            return

        sleep(1)  # simulando o tempo de um acesso a base de dados, etc
        self.estoque -= quantidade
        print(f'Você comprou {quantidade} ingressos. '
              f'Ainda temos {self.estoque}')
        self.lock.release()  # liberando para que a proxima execucao da instancia entre na funcao


if __name__ == '__main__':
    ingressos = Ingresso(10)

    threads = []
    for i in range(1, 10):
        t = Thread(target=ingressos.comprar, args=(i,))
        # ingressos.comprar(i)  #forma direta de executar a classe
        threads.append(t)  # pegando o resultado de execuçao das chamadas da funcao comprar
    for t in threads:
        t.start()

    executando = True
    while executando:
        executando = False

        for t in threads:
            if t.is_alive():
                executando = True
                break
    print(ingressos.estoque)
