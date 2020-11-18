# a tabela de banco de dados foi criada atraves da ferramenta DB Browser

import sqlite3


class AgendaDB:
    def __init__(self, arquivo):
        self.conn = sqlite3.connect(arquivo)
        self.cursor = self.conn.cursor()

    def inserir(self, nome, telefone):
        consulta = 'INSERT OR IGNORE INTO agenda (nome, telefone) VALUES (?, ?)'
        self.cursor.execute(consulta, (nome, telefone))
        self.conn.commit()

    def editar(self, nome, telefone, id):
        editar = 'UPDATE OR IGNORE agenda SET nome=?, telefone=? WHERE id=?'
        self.cursor.execute(editar, (nome, telefone, id))
        self.conn.commit()

    def excluir(self, id):
        exclui = 'DELETE FROM agenda WHERE id=?'
        self.cursor.execute(exclui, (id,))
        self.conn.commit()

    def listar(self):
        self.cursor.execute('SELECT * FROM agenda')
        for linha in self.cursor.fetchall():
            print(linha)

    def buscar(self, valor):
        busca = 'SELECT * FROM agenda WHERE nome LIKE ?'
        self.cursor.execute(busca, (f'%{valor}%',))

        for linha in self.cursor.fetchall():
            print(linha)


    def fechar(self):
        self.cursor.close()
        self.conn.close()


if __name__ == '__main__':
    agenda = AgendaDB('agenda.db')
    # agenda.inserir('Joãozinho', '111111')
    # agenda.inserir('Maria', '222222')
    # agenda.inserir('Rose', '333333')
    # agenda.inserir('Guilherme', '444444')
    # agenda.inserir('Fabricio', '555555')
    # agenda.inserir('Joãozinho', '666666')

    # agenda.inserir('Luiz Otavio', '123456')
    # agenda.inserir('Luiz Felipe', '654321')
    # agenda.inserir('Luiz Romano', '254136')
    # agenda.inserir('R. Luiza', '365214')
    # agenda.inserir('R. Luiza Meio do Caminho', '365211')
    # agenda.editar('Francisco', '121212', 13)
    # agenda.excluir(13)
    # agenda.listar()
    agenda.buscar('Luiz')
