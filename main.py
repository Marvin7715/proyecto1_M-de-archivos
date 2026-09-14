import sys

from PyQt6.QtWidgets import QApplication, QLabel, QWidget


app = QApplication(sys.argv)

ventana = QWidget()
ventana.setWindowTitle("Proyecto Manejo de Archivos")
ventana.resize(500, 300)

texto = QLabel("PyQt6 funciona correctamente", parent=ventana)
texto.move(150, 130)

ventana.show()

sys.exit(app.exec())