"""
criando uma conta abstrata parqa que ela seja manipulada pelas classes filhas,
sem poder ser instanciada
"""
from clAbstrato import Conta, ContaPoupanca, ContaCorrente

cp = ContaPoupanca(111, 222, 0)
cp.depositar(10)
cp.sacar(10)
cp.sacar(1)

print(10 * '======')
cc = ContaCorrente(123456, 5555, 500)
cc.depositar(100)
cc.sacar(700)
cc.sacar(100)

