from clcomposicao import Endereco, Cliente

cl1 = Cliente('Luiz', 32)
cl1.insere_end('Belo Horizonte', 'MG')
print(cl1.nome)
cl1.lislta_endereco()

cl2 = Cliente('Maria', 42)
cl2.insere_end('Paraná', 'PR')
cl2.insere_end('Rio de Janeiro', 'RJ')
print(cl2.nome)
cl2.lislta_endereco()

cl3 = Cliente('Joãozinho', 19)
cl3.insere_end('São Paulo', 'SP')
print(cl3.nome)
cl3.lislta_endereco()

print(10 * '=====')
