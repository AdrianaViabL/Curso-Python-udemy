# molde inicial de pessoas
from datetime import datetime


class Pessoa:
    ano_atu = int(datetime.strftime(datetime.now(), '%Y'))

    def __init__(self, nome, idade, comendo=False,
                 falando=False):  # por convenção é usado SELF como forma de refenciar o endereco da propria instancia
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def falar(self, asssunto):  # o self é uma forma de refernciar a propria instancia
        if self.comendo:
            print(f'{self.nome} não pode falar comendo')
            return
        if self.falando:
            print(f'{self.nome} já está falando')
            return

        print(f'{self.nome} falando sobre {asssunto}')
        self.falando = True

    def parar_falar(self):
        if not self.falando:
            print(f'{self.nome} não esta falando')
            return
        print(f'{self.nome} parou de falar')
        self.falando = False

    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} já está comendo.')
            return  # nao vai executar nada mais a baixo do return quando cair nessa condição
        if self.falando:
            print(f'{self.nome} não pode comer falando')
            return
        print(f'{self.nome} está comendo {alimento}')
        self.comendo = True

    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo.')
            return
        print(f'{self.nome} parou de comer')
        self.comendo = False

    def get_ano_nascimento(self):
        return self.ano_atu - self.idade
