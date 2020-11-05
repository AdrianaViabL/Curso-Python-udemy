class Banco:
    def __init__(self):
        self.__agencia = []
        self.__cliente = []
        self.__conta = []

    @property
    def agencia(self):
        return self.__agencia

    @agencia.setter
    def agencia(self, agencia):
        self.__agencia.append(agencia)

    @property
    def conta(self):
        return self.__conta

    @conta.setter
    def conta(self, conta):
        self.__conta.append(conta)

    @property
    def cliente(self):
        return self.__cliente

    @cliente.setter
    def cliente(self, cliente):
        self.__cliente.append(cliente)

    def insere_cliente(self, cliente):
        self.cliente.append(cliente)

    def insere_conta(self, conta):
        self.conta.append(conta)
        self.agencia.append(conta.agencia)

    def valida_conta(self, cliente):
        if cliente not in self.cliente:
            print('conta nao existe nesse banco')
            return False

        if cliente.conta not in self.conta:
            print('cliente nao existe nesse banco')
            return False

        if cliente.conta.agencia not in self.agencia:
            print('agencia nao existe nesse banco')
            print(self.agencia, ' = ', cliente.conta.agencia)
            return False

        return True
