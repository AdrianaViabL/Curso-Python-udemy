class Eletronico:
    def __init__(self, nome):
        self.__nome = nome
        self._ligado = False

    def ligar(self):
        if self._ligado:
            return
        self._ligado = True  

    def desligar(self):
        if not self._ligado:
            return
        self._ligado = False

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome


class LogMixin:  # classe que ira gerar um 'arquivo de log'
    @staticmethod
    def write(msg):
        with open('log.log', 'a+') as f:
            f.write(msg)
            f.write('\n')

    def log_info(self, msg):
        self.write(f'INFO:{msg}')

    def log_error(self, msg):
        self.write(f'Error:{msg}')


class Celular(Eletronico, LogMixin):
    def __init__(self, nome):
        super().__init__(nome)
        self._conectado = False

    def conectar(self):
        if not self._ligado:
            erro = f'{self.nome} não está ligado'
            print(erro)
            self.log_info(erro)
            return
        if self._conectado:
            erro = f'{self.nome} Já esta conectado!'
            print(erro)
            self.log_info(erro)
            return
        self._conectado = True
        info = f'{self.nome} foi conectado com sucesso!'
        print(info)
        self.log_info(info)

    def desconectar(self):
        if not self._conectado:
            erro = f'{self.nome} NÃO esta conectado!'
            print(erro)
            self.log_info(erro)
            return
        self._conectado = False
        info = f'{self.nome} foi desconectado com sucesso!'
        print(info)
        self.log_info(info)
