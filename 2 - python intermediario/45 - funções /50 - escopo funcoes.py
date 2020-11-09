variavel = 'valor'
print(variavel)
def func():
    global variavel
    variavel = 'outro valor'
    print(variavel)


func()
#É ERRADO ALTERAR O VALOR DE UMA VARIAVEL GLOBAL
# DENTRO DE UMA FUNÇAO POIS PODE HAVER UM COMPORTAMENTO INESPERADO
print('novo valor da variavel = ', variavel)
nova_var = 'valor'
def func2(arg=None):
    arg = arg.replace('v', 'c')
    return arg

novo_val = func2(nova_var)
print(novo_val)
print('valor ainda sendo o mesmo ', nova_var)












