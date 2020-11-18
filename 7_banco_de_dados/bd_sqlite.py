import sqlite3

conexao = sqlite3.connect('basedados.db')
cursor = conexao.cursor()  # para executar comandos SQL dentro do banco de dados

cursor.execute('CREATE TABLE IF NOT EXISTS cliente ('  # criando uma tabela
               'id INTEGER PRIMARY KEY AUTOINCREMENT,'  # criando o indice da tabela -  nome tipo de dado
               'nome TEXT,'  # campo tipo string
               'peso REAL'  # campo tipo float
               ')')
# varias formas de inserir dados na tabela
# cursor.execute('INSERT INTO cliente (nome, peso) VALUES (?, ?)', ('Maria', 60))  # preenchendo a tabela
# cursor.execute('INSERT INTO cliente (nome, peso) VALUES (:nome, :peso)',
#                {'nome': 'Zezinho', 'peso': 80.6})
# cursor.execute('INSERT INTO cliente VALUES (:id, :nome, :peso)',
#                {'id': None, 'nome': 'qualquer', 'peso': 180})
#
# conexao.commit() #salvando os dados alterados ate o momento

# cursor.execute('UPDATE cliente SET nome=:nome WHERE id=:id',
#                {'nome': 'Joana', 'id': 7})
#
# cursor.execute('DELETE FROM cliente WHERE id=:id',
#                {'id': 7})
# cursor.execute('SELECT * FROM cliente')

cursor.execute('SELECT nome, peso FROM cliente WHERE peso > 80')  # um select mais especifico

# cursor.execute('DELETE FROM cliente')
# conexao.commit()

for linha in cursor.fetchall():
    nome, peso = linha
    print(nome, peso)

cursor.close()
conexao.close()
