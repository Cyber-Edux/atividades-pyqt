import sys
from PySide6.QtWidgets import *
from main_window import Ui_MainWindow  # Importa a interface gerada


class MinhaJanela(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Exemplo: conectar botão a uma função
        self.ui.say_hello_button.clicked.connect(self.dizer_ola)


    def dizer_ola(self):
        nome = self.ui.name_input.text()
        QMessageBox.information(self, 'Olá!', f'Oi, {nome}!')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = MinhaJanela()
    janela.show()
    sys.exit(app.exec())
