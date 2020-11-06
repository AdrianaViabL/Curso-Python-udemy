import sys
from usando_qtdesigner148.design import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.QtGui import QPixmap


class Redimensionamento(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)  # para que ele execute a instancia dessa classe
        self.btnEscolheArq.clicked.connect(self.abrir_imagem)
        self.btnRedim.clicked.connect(self.redimensionar)
        self.btnSalvar.clicked.connect(self.salvar)

    def abrir_imagem(self):
        image, _ = QFileDialog.getOpenFileName(
            self.centralwidget,
            'Abrir imagem'
            '/home/adriana/Downloads/',
            # options=QFileDialog.DontUseNativeDialog  #se nao funcionar a janela, descomentar essa parte

        )
        self.inputArquivo.setText(image)
        self.original_img = QPixmap(image)
        self.labelImg.setPixmap(self.original_img)
        self.inputLargura.setText(str(self.original_img.width()))
        self.inputAltura.setText(str(self.original_img.height()))

    def redimensionar(self):
        largura = int(self.inputLargura.text())
        self.nova_imagem = self.original_img.scaledToWidth(largura)  # calcula a altura automaticamente
        self.labelImg.setPixmap(self.nova_imagem)
        self.inputLargura.setText(str(self.nova_imagem.width()))
        self.inputAltura.setText(str(self.nova_imagem.height()))

    def salvar(self):
        image, _ = QFileDialog.getSaveFileName(
            self.centralwidget,
            'Salvar imagem'
            '/home/adriana/',
        )
        self.nova_imagem.save(image)


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    novo = Redimensionamento()
    novo.show()
    qt.exec_()
