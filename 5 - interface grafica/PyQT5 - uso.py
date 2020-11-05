"""
PyQT é um tookit desenvolvido em C++ utilizado por varios programas
para a criação de aplicações GUI(interface gráfica). Tambem inclui
diversas funcionalidades, como: acesso a base de dados, threads,
comunicação de rede, etc...
"""
import sys
from PyQt5.QtWidgets import QMainWindow, \
    QApplication, QPushButton, QWidget, QGridLayout
# sao as principais classes usadas com o PyQT5 para gerar uma interface



class App(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)
        self.btn = QPushButton('texto botao')
        self.grid.addWidget(self.btn, 0, 0, 1, 1)#adicionando o botao a grid
        #parametros do addWidget = pos linha, pos coluna, qtd linha ocupadas,
        # qtd colunas ocupadas

        self.btn.clicked.connect(lambda: print('olá mundo \o/')) #dando uma ação ao botão
        self.btn.clicked.connect(self.acao)#usando uma função para executar uma ação

        self.setCentralWidget(self.cw)
    def acao(self):
        print('alguma coisa')


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    app = App()
    app.show()
    qt.exec_()
