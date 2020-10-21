"""
Estudo inicial de POO, com a representação do mundo real em codigo
"""
from pessoa import Pessoa

p1 = Pessoa('Adriana', 26)  # instanciando uma classe
p2 = Pessoa('João', 32)
print('sendo feito a mesma atribuição, so que depois de criadas as instancias das classes')
p1.nome = 'Adriana'  # acrecentando um valor em apenas umas das instancias da classe Pessoa
p2.nome = 'João'
print(p1)  #eles tem endereco de memoria diferente entre si
print(p2)
print(p2.nome)


p1.comer('maçã')  #para evitar que ele 'coma' duas coisas ao mesmo tempo, a validação deve ser feita na classe que esta sendo executada
p1.parar_comer()
p1.parar_comer()

p1.falar('gatos')
p1.falar('tartaruga')
p1.comer('ssss')
p1.parar_falar()
p1.comer('qualquer coisa')


p2.comer('torta')

print('como sao duas instancias independentes, pode-se mandar "fazer a mesma coisa ao mesmo tempo"')

print(p1.ano_atu)
print(Pessoa.ano_atu)  #tendo acesso a uma variavel dentro da classe sem instancia-la

print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())
