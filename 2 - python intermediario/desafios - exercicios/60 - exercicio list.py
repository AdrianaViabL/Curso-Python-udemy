'''
separar os valores iguais e montar eles separados por
ponto em uma nova string
'''

string = '012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789'
n = 10

separa = [string[v:v + n] for v in range(0, len(string), n)]
junta = '.'.join(separa)
print(junta)
