"""
Diferença basica: Lista pode ter seu valor alterado,
já a tupla nao pode ter seu valor alterado
"""
t1 = (1, 2, 3, 'a', 'Adriana')

print(t1[:2])

t2 = 1, 2, 3, 'adriana', 'valor qualquer'  #Não e necessario o uso de parentese para declarar uma tupla

n1, n1, n3, *_ = t2

print(_)
