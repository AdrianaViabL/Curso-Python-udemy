class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeClasse = self.__class__.__name__  # pegando o nome da classe

    def falando(self):
        print(f'{self.nomeClasse} está falando...')


class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.nomeClasse} está comprando...')

    def falando(self):
        print('passando pela classe Cliente')


class ClienteVIP(Cliente):  # cadeia de herança
    def __init__(self, nome, idade, sobrenome):
        # Pessoa.__init__(nome, idade)  #é possivel tambem chamar a classe diretamente
        super().__init__(nome, idade)  # copiando o construtor da classe Pessoa, para que nao haja sobreposição
        self.sobrenome = sobrenome

    def falando(self):
        # super().falando() para pegar a declaração da classe a cima da VIP(que seria Cliente)
        Pessoa.falando(self)
        Cliente.falando(self)
        print('sobrepondo o metodo falar no VIP')


class Aluno(Pessoa):
    def estudar(self):
        print(f'{self.nomeClasse} está estudando...')
