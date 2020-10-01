"""
Tipos de dados
str - string - texto
int -inteiro - numeros int   eiros
float - real/ponto flutuante
bool - boolenano/logico - true ou false

na conversao os valores vazios(uma lista vazia) e false
"""
print('nome', 'isso é uma', type('nome'))
print(123456, 'isso é uma', type(123456))
print(10.1, 'isso é uma', type(10.1))
print(10 == 10, 'isso é uma', type(10 == 10))

print('10', type('10'), type(int('10')))  # mostrando primeiramente como uma string e
                                          # depois convertendo o valor para inteiro
#atividade extra
idade = 26
print(10 * '=========')

print('nome','Adriana', type('Adriana'))
print('idade', idade, type(idade))
print('altura', 1.70, type(1.70))
print(idade > 18, type(idade > 18))

