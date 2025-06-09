from PySide6.QtWidgets import (
    QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QMessageBox, QComboBox
)
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora Simples")

        # Elementos da interface
        self.label_a = QLabel("Número A:")
        self.input_a = QLineEdit()

        self.label_b = QLabel("Número B:")
        self.input_b = QLineEdit()

        self.operacao = QComboBox()
        self.operacao.addItems(["soma", "subtração", "multiplicação", "divisão", "potenciação"])

        self.botao_calcular = QPushButton("Calcular")
        self.botao_calcular.clicked.connect(self.calcular)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.label_a)
        layout.addWidget(self.input_a)
        layout.addWidget(self.label_b)
        layout.addWidget(self.input_b)
        layout.addWidget(self.operacao)
        layout.addWidget(self.botao_calcular)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def calcular(self):
        a = float(self.input_a.text())
        b = float(self.input_b.text())
        operacao = self.operacao.currentText()

        if operacao == "soma":
            resultado = a + b
        elif operacao == "subtração":
            resultado = a - b
        elif operacao == "multiplicação":
            resultado = a * b
        elif operacao == "divisão":
            resultado = a / b if b != 0 else float('nan')
        elif operacao == "potenciação":
            resultado = a ** b
        else:
            resultado = float('nan')

        QMessageBox.information(self, "Resultado", f"Resultado: {resultado}")
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = MainWindow()
    janela.show()
    sys.exit(app.exec())
