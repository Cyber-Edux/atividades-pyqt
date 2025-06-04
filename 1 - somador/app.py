from PySide6.QtWidgets import (
    QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QMessageBox
)
import sys

class MainWindow(QMainWindow): # Janela Principal
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora Simples") # Título da janela

        # Elementos da interface
        self.label_a = QLabel("Número A:") # Uma QLabel é um pequeno texto na interface
        self.input_a = QLineEdit() # Um QLineEdit é uma caixa de digitar texto

        self.label_b = QLabel("Número B:") 
        self.input_b = QLineEdit()

        self.botao_calcular = QPushButton("Calcular") 
        self.botao_calcular.clicked.connect(self.calcular)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.label_a)
        layout.addWidget(self.input_a)
        layout.addWidget(self.label_b)
        layout.addWidget(self.input_b)
        layout.addWidget(self.botao_calcular)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def calcular(self):
        try:
            a = float(self.input_a.text())
            b = float(self.input_b.text())
            resultado = a + b
            QMessageBox.information(self, "Resultado", f"A + B = {resultado}")
        except ValueError:
            QMessageBox.warning(self, "Erro", "Por favor, insira números válidos.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = MainWindow()
    janela.show()
    sys.exit(app.exec())
