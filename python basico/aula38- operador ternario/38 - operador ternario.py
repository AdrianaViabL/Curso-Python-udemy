logged_user = False
if logged_user:
    msg = 'Usuário logado'
else:
    msg = 'Usuário precisa logar'
print(msg)

print('simplificando a atribuição de valor em uma variavel')
logged_user = True
msg = 'Usuário logado' if logged_user else 'Usuário precisa logar'
print(msg)

print(10 * '===')
idade = input('qual a sua idade: ')
if not idade.isnumeric():
    print('Voce precisa digitar apenas números')
else:
    idade = int(idade)
    maior_idade = (idade >= 18)
    msg = 'pode acessar' if maior_idade else 'Não pode acessar'
    print(msg)
