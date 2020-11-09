import sys
from CPF149.validaCPF import valida_cpf
from CPF149.geraCPF import gera_cpf
from PyQt5.QtWidgets import QApplication, QMainWindow
from CPF149.design import Ui_MainWindow


class GeraValidaCPF(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.btnGerarCPF.clicked.connect(self.gera_cpf)
        self.btnValidaCPF.clicked.connect(self.valida_cpf)

    def gera_cpf(self):
        self.labelRetorno.setText(
            gera_cpf()
        )

    def valida_cpf(self):
        cpf = self.inputValidacpf.text()
        self.labelRetorno.setText(
            str(valida_cpf(cpf))
        )


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    gera_valida = GeraValidaCPF()
    gera_valida.show()
    qt.exec_()
