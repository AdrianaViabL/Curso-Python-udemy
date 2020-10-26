"""
Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar/depositar nessa conta. Contas corrente tem um limite extra. Banco
tem clientes e contas.

Dicas:
Criar classe Cliente que herda da classe Pessoa (Herança)
    Pessoa tem nome e idade (com getters)
    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)
Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
    ContaCorrente deve ter um limite extra
    Contas têm agência, número da conta e saldo
    Contas devem ter método para depósito
    Conta (super classe) deve ter o método sacar abstrato (Abstração e
    polimorfismo - as subclasses que implementam o método sacar)
Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
Banco será responsável autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clentes (Agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco
Só será possível sacar se passar na autenticação do banco (descrita acima)
"""
from contas import ContaCorrente, ContaPoupanca
from cliente import Cliente
from banco import Banco

banco = Banco()
p1 = Cliente('pessoa', 28)
p2 = Cliente('Joãozinho', 50)
p3 = Cliente('Maria', 18)

c1 = ContaPoupanca(321, 231, 0)
c2 = ContaCorrente(123, 521, 0, 100)
c3 = ContaCorrente(789, 521312, 0, 1000)

p1.insere_conta(c1)
p2.insere_conta(c2)
p3.insere_conta(c3)

p1.conta.deposita(50)
p1.conta.mostra_saldo()
p1.conta.sacar(20)
p1.conta.mostra_saldo()
print(10 * '====')
banco.insere_cliente(p1)
banco.insere_conta(c1)

if banco.valida_conta(p1):
    p1.conta.deposita(520)
    p1.conta.mostra_saldo()
    p1.conta.sacar(10)

if banco.valida_conta(p2):
    p2.conta.deposita(520)
    p2.conta.mostra_saldo()
    p2.conta.sacar(1000)

banco.insere_cliente(p3)
banco.insere_conta(c3)
print(10 * '====')
if banco.valida_conta(p3):
    p3.conta.deposita(520)
    p3.conta.mostra_saldo()
    p3.conta.sacar(1000)
    p3.conta.mostra_saldo()
