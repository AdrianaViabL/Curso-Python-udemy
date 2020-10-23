"""
https://rszalski.github.io/magicmethods/
"""


class A:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls,
                       '_jaexiste'):  # forma de fazer com que essa classe seja instanciada mais de uma vez, ou seja sempre vao ter o mesmo endereco de memoria
            cls._jaexiste = super().__new__(cls)
        return cls._jaexiste
        print('eu sou o NEW')
        cls.nome = 'qualquer coisa'
        return super().__new__(cls)
        # return object.__new__(cls) - sao a mesma coisa

    def __init__(self):
        print('Eu sou INIT')

    def __call__(self, *args, **kwargs):
        print(args)
        print(kwargs)
        resultado = 1
        for i in args:
            resultado *= i
        return resultado

    def __setattr__(self, key, value):  # setando novas variaveis dentro da classe de acordo com o que usuario digitar
        self.__dict__[key] = value
        print(key, value)

    def __str__(self):
        return 'transformando a classe em uma string'

    def __len__(self):
        return 55

    def __del__(self):
        print('objeto coletado pel Garbage Colector do PYTHON')


a = A()
b = A()
c = A()
print(c)

print(type(a))
print(a == b)
# print(a.nome)
a(1, 2, 3, 4, 5, 6, nome='Luiz')
b = A()
valr = b(5, 5, 1, 1, 2)
print(valr)
b.nome = ' qualquer coisa'
print(len(a))   #alterando o comportamento da função LEN com o metodo magico