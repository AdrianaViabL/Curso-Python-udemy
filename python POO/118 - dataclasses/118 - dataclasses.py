"""
O que são dataclasses? O módulo Dataclasses fornece um decorador e funções
para criar automaticamente métodos, como __init__(), __repr__(), __eq__ (etc)
em classes definidas pelo usuário.
Basicamente, dataclasses são syntax sugar para criar classes normais.
Foi originalmente descrito na PEP 557.
Adicionado na versão 3.7 do Python.
Leia a documentação: https://docs.python.org/pt-br/3/library/dataclasses.html
"""
# o dataclass nao funciona bem com herança
from dataclasses import dataclass, field, asdict, astuple


@dataclass(eq=False, init=True, repr=True)  # voce pode ativar ou desativar parametros de dentro do dataclass
class Pessoa:
    nome: str
    sobrenome: str = field(repr=False)

    def __post_init__(self):  # comando que sera executado depois do init
        if not isinstance(self.nome, str):
            raise TypeError(
                f'Tipo invalido {type(self.nome).__name__} != str em {self}')

    @property
    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'


p1 = Pessoa('Luiz', 'Otavio')
print(p1)
print(p1.nome_completo)

print(asdict(p1))  # transformando num dicionario
print(astuple(p1))  # transformando em tupla
