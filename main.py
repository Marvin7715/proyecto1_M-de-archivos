import sys

from PyQt6.QtWidgets import QApplication

from ui.main_window import MainWindow


def main():
    aplicacion = QApplication(sys.argv)

    ventana = MainWindow()
    ventana.show()

    sys.exit(aplicacion.exec())


if __name__ == "__main__":
    main()