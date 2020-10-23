from clHeranca import Cliente, Aluno, ClienteVIP, Pessoa
c1 = Cliente('Adriana', 26)
c2 = Aluno('João', 30)
c3 = ClienteVIP('teste', 111, 'da silva')

c1.falando()
c1.falando()
c2.falando()
c2.estudar()
print(10 * '====')
c3.falando()  #classe que herdou caracteristicas tanto de Pessoa como de Cliente

c4 = Pessoa('classe', 50)
