import sys
from PySide6.QtWidgets import *
from main_window import Ui_MainWindow


class MainWindow(QMainWindow):
    # Classe da janela principal
    def __init__(self):
        super().__init__()
        # --- Construir a interface ---
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # --- Conectar signals e slots ---
        botoes_de_digitacao = [ # Lista de botões de digitação
            self.ui.lbracketPushButton,
            self.ui.rbracketPushButton,
            self.ui.powPushButton,
            self.ui.plusPushButton,
            self.ui.minusPushButton,
            self.ui.mulPushButton,
            self.ui.divPushButton,
            self.ui.pushButton0,
            self.ui.pushButton1,
            self.ui.pushButton2,
            self.ui.pushButton3,
            self.ui.pushButton4,
            self.ui.pushButton5,
            self.ui.pushButton6,
            self.ui.pushButton7,
            self.ui.pushButton8,
            self.ui.pushButton9
        ]
        for botao in botoes_de_digitacao:
            # Conectar o signal 'clicked' dos botões de digitação ao slot 'slot_de_digitacao'
            botao.clicked.connect(self.slot_de_digitacao)
    
        # Conectar os signals 'clicked' dos botões de limpar e resultado aos respectivos slots
        self.ui.clsPushButton.clicked.connect(self.slot_limpar)
        self.ui.eqPushButton.clicked.connect(self.slot_resolver)


    def slot_de_digitacao(self):
        # Método que é executado quando qualquer botão de digitação é clicado
        botao_clicado: QPushButton = self.sender() # Obter botão que foi clicado
        simbolo = botao_clicado.text() # Texto do botão clicado
        expressao_atual = self.ui.lineEdit.text() # Texto atual do lineEdit
        expressao_modificada = expressao_atual + simbolo # Expressão com adição do símbolo
        self.ui.lineEdit.setText(expressao_modificada) # Atualizar texto do lineEdit


    def slot_limpar(self):
        self.ui.lineEdit.clear() # Limpar o lineEdit


    def slot_resolver(self):
        # Método que é executado quando o botão '=' é clicado
        expressao = self.ui.lineEdit.text() # Obtem a expressão do lineEdit
        try:
            resultado = eval(expressao) # Resolver a expressão
            QMessageBox.information(self, 'Resultado', f'O resultado é {resultado}') # Mostrar resultado
        except Exception as ex:
            QMessageBox.warning(self, 'Erro', str(ex)) # Mostrar msg de erro


if __name__ == '__main__':
    app = QApplication(sys.argv) # Instanciar app do Qt
    win = MainWindow() # Instanciar janela
    win.show() # Mostrar janela
    sys.exit(app.exec()) # Criar loop de eventos