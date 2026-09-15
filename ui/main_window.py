import os

from PyQt6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QLabel,
    QMenuBar,
    QMessageBox
)
from PyQt6.QtGui import QAction, QPixmap
from PyQt6.QtCore import Qt

from config_manager import cargar_configuracion, guardar_configuracion
from .settings_window import SettingsWindow

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.configuracion = cargar_configuracion()

        self.setWindowTitle("Manejo de Archivos - Configuración de Usuario")
        self.resize(900, 600)

        self.crear_interfaz()
        self.crear_menu()
        self.aplicar_configuracion()
        self.aplicar_foto_perfil()

    def crear_interfaz(self):
        widget_central = QWidget()
        layout = QVBoxLayout()

        self.titulo = QLabel("Manejo de Archivos")
        self.titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.subtitulo = QLabel("Configuración de Usuario")
        self.subtitulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.foto_perfil = QLabel()
        self.foto_perfil.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout.addStretch()
        layout.addWidget(self.titulo)
        layout.addWidget(self.subtitulo)
        layout.addWidget(self.foto_perfil)
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

    def aplicar_configuracion(self):
        tema = self.configuracion["tema_interfaz"]
        tamaño_fuente = self.configuracion["tamaño_fuente"]
        color_menu = self.configuracion["color_barra_menu"]
        color_letra = self.configuracion["color_letra"]

        if tema == "oscuro":
            color_fondo = "#202124"
        else:
            color_fondo = "#FFFFFF"

        self.setStyleSheet(
            f"""
            QMainWindow {{
                background-color: {color_fondo};
            }}

            QLabel {{
                color: {color_letra};
                font-size: {tamaño_fuente}px;
            }}

            QMenuBar {{
                background-color: {color_menu};
                color: {color_letra};
                font-size: {tamaño_fuente}px;
            }}

            QMenuBar::item {{
                background-color: transparent;
                padding: 5px 10px;
            }}

            QMenu {{
                background-color: {color_fondo};
                color: {color_letra};
                font-size: {tamaño_fuente}px;
            }}

            QPushButton {{
                font-size: {tamaño_fuente}px;
            }}
            """
        )

    def opcion_no_disponible(self):
        QMessageBox.information(
            self,
            "Opción simulada",
            "Esta opción es únicamente demostrativa."
        )

    def abrir_settings(self):
        ventana_settings = SettingsWindow(
            self.configuracion,
            self
        )

        if ventana_settings.exec():
            self.configuracion = ventana_settings.configuracion

            if guardar_configuracion(self.configuracion):
                self.aplicar_configuracion()
                self.aplicar_foto_perfil()

                QMessageBox.information(
                    self,
                    "Configuración",
                    "La configuración se guardó correctamente."
                )
            else:
                QMessageBox.critical(
                    self,
                    "Error",
                    "No fue posible guardar la configuración."
                )

    def aplicar_foto_perfil(self):
        ruta_foto = self.configuracion["foto_perfil"]

        if ruta_foto and os.path.exists(ruta_foto):
            imagen = QPixmap(ruta_foto)

            if not imagen.isNull():
                imagen = imagen.scaled(
                    150,
                    150,
                    Qt.AspectRatioMode.KeepAspectRatio,
                    Qt.TransformationMode.SmoothTransformation
                )

                self.foto_perfil.setPixmap(imagen)
                return

        self.foto_perfil.setText("Sin foto de perfil")