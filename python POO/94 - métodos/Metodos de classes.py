import random


class Pessoa:
    ano_atual = 2020

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nasc(self):
        print(self.ano_atual - self.idade)

    @classmethod
    def por_ano_nasc(cls, nome, ano_nasc):
        idade = cls.ano_atual - ano_nasc
        return cls(nome, idade)

    @staticmethod  #metodo estatico, onde nao pode usar a classe(self ou cls)
    def gera_id():
        rand = random.randint(10000, 19999)
        return rand

p1 = Pessoa('Luiz', 32)
print(p1)
print(p1.nome, p1.idade)
p1.get_ano_nasc()
print(Pessoa.gera_id())
print(p1.gera_id())
