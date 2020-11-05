from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, agencia, conta, saldo=0):
        self.__agencia = agencia
        self.__conta = conta
        self.saldo = saldo

    @property
    def agencia(self):
        return self.__agencia

    @property
    def conta(self):
        return self.__conta

    @agencia.setter
    def agencia(self, agencia):
        self.__agencia = agencia

    @conta.setter
    def conta(self, conta):
        self.__conta = conta

    def deposita(self, valor):
        if not isinstance(valor, int):
            print('valor de deposito tem que ser numerico!!!')
            return
        self.saldo += valor

    def mostra_saldo(self):
        print(f'saldo na agencia:{self.agencia} conta: {self.conta} = {self.saldo}')

    @abstractmethod
    def sacar(self, valor):
        pass


class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo=0, limite=0):
        super().__init__(agencia, conta, saldo)
        self.limite = limite

    def sacar(self, valor):
        if (valor + self.limite) < self.saldo:
            print('sem saldo para sacar')
            return
        self.saldo -= valor


class ContaPoupanca(Conta):
    def __init__(self, agencia, conta, saldo):
        super().__init__(agencia, conta, saldo)

    def sacar(self, valor):
        if self.saldo < valor:
            print('saldo insuficiente para saque!')
            return
        self.saldo -= valor
