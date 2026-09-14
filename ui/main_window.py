from PyQt6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QLabel,
    QMenuBar,
    QMessageBox
)
from PyQt6.QtGui import QAction
from PyQt6.QtCore import Qt


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Manejo de Archivos - Configuración de Usuario")
        self.resize(900, 600)

        self.crear_interfaz()
        self.crear_menu()

    def crear_interfaz(self):
        widget_central = QWidget()
        layout = QVBoxLayout()

        titulo = QLabel("Manejo de Archivos")
        titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        subtitulo = QLabel("Configuración de Usuario")
        subtitulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout.addStretch()
        layout.addWidget(titulo)
        layout.addWidget(subtitulo)
        layout.addStretch()

        widget_central.setLayout(layout)

        self.setCentralWidget(widget_central)

    def crear_menu(self):
        barra_menu = QMenuBar()

        menu_archivo = barra_menu.addMenu("Archivo")
        menu_edicion = barra_menu.addMenu("Edición")
        menu_ver = barra_menu.addMenu("Ver")
        menu_settings = barra_menu.addMenu("Settings")

        opcion_nuevo = QAction("Nuevo", self)
        opcion_abrir = QAction("Abrir", self)
        opcion_guardar = QAction("Guardar", self)
        opcion_salir = QAction("Salir", self)

        menu_archivo.addAction(opcion_nuevo)
        menu_archivo.addAction(opcion_abrir)
        menu_archivo.addAction(opcion_guardar)
        menu_archivo.addSeparator()
        menu_archivo.addAction(opcion_salir)

        opcion_copiar = QAction("Copiar", self)
        opcion_pegar = QAction("Pegar", self)

        menu_edicion.addAction(opcion_copiar)
        menu_edicion.addAction(opcion_pegar)

        opcion_modo = QAction("Vista", self)
        opcion_informacion = QAction("Información", self)

        menu_ver.addAction(opcion_modo)
        menu_ver.addAction(opcion_informacion)

        opcion_configuracion = QAction("Configuración de usuario", self)
        menu_settings.addAction(opcion_configuracion)

        opcion_nuevo.triggered.connect(self.opcion_no_disponible)
        opcion_abrir.triggered.connect(self.opcion_no_disponible)
        opcion_guardar.triggered.connect(self.opcion_no_disponible)
        opcion_copiar.triggered.connect(self.opcion_no_disponible)
        opcion_pegar.triggered.connect(self.opcion_no_disponible)
        opcion_modo.triggered.connect(self.opcion_no_disponible)
        opcion_informacion.triggered.connect(self.opcion_no_disponible)

        opcion_salir.triggered.connect(self.close)
        opcion_configuracion.triggered.connect(self.abrir_settings)

        self.setMenuBar(barra_menu)

    def opcion_no_disponible(self):
        QMessageBox.information(
            self,
            "Opción simulada",
            "Esta opción es únicamente demostrativa."
        )

    def abrir_settings(self):
        QMessageBox.information(
            self,
            "Settings",
            "Aquí construiremos la ventana de configuración."
        )