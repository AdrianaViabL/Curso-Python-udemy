'''
funções pt 1

'''


def funcao():
    print('ola mundo')


funcao()  #usando a função criada


def saudacao(msg='Olá', nome='usuário'):
    nome = nome.replace('e', '3')
    print(msg, nome)

saudacao()  #sem parametro enviados, eme mostra o que foi declarado como padrao
saudacao('ola ', 'nome qualquer')
saudacao(nome='Zezinho', msg='hello!!')  #quando se trabalha com o nome da variavel existente na função se pode inverter sua declaração
