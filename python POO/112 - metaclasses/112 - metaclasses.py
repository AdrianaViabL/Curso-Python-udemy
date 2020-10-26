"""
em python tudo e um objeto, incluindo as classes
metaclasses sao as 'classes' que criam classes

"""


class Meta(type):
    def __new__(mcs, name, bases, namespace):
        if name == 'A':
            return type.__new__(mcs, name, bases, namespace)

        if 'attr_classe' in namespace:  # evitando que outras classes sobrescrevam a funcao criada em A
            print(f'{name} tentou sobrescrever o atributo')
            del namespace['attr_classe']
        return type.__new__(mcs, name, bases, namespace)


class A(metaclass=Meta):
    attr_classe = 'Valor A'

    def fala(self):
        print('ola')


class B(A):
    attr_classe = 'Valor B'


class C(B):
    attr_classe = 'Valor B'


c = C()
print(c.attr_classe)
