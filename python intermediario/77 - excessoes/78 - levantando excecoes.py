"""
https://docs.python.org/3/library/exceptions.html
"""

def divide(n1, n2):
    if n2 == 0 or n1 == 0:
        raise ValueError('nao pode ter numero zero')
    return n1 / n2

try:
    print(divide(10, 0))
except ValueError as erro:
    print(erro)

