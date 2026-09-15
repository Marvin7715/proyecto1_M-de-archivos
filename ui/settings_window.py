import os
import shutil

from PyQt6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QFormLayout,
    QLineEdit,
    QComboBox,
    QSpinBox,
    QPushButton,
    QColorDialog,
    QFileDialog,
    QLabel,
    QMessageBox
)
from PyQt6.QtGui import QPixmap


class SettingsWindow(QDialog):

    def __init__(self, configuracion, parent=None):
        super().__init__(parent)

        self.configuracion = configuracion.copy()

        self.setWindowTitle("Settings - Configuración de Usuario")
        self.setFixedSize(500, 500)

        self.crear_interfaz()
        self.cargar_datos()

    def crear_interfaz(self):
        layout_principal = QVBoxLayout()

        formulario = QFormLayout()

        self.campo_nombre = QLineEdit()

        self.combo_tema = QComboBox()
        self.combo_tema.addItems(["claro", "oscuro"])

        self.combo_idioma = QComboBox()
        self.combo_idioma.addItems(["es", "es-ES", "en", "en-US"])

        self.campo_fuente = QSpinBox()
        self.campo_fuente.setMinimum(8)
        self.campo_fuente.setMaximum(48)

        self.boton_color_menu = QPushButton("Seleccionar color")
        self.boton_color_letra = QPushButton("Seleccionar color")
        self.boton_foto = QPushButton("Seleccionar foto")

        self.etiqueta_foto = QLabel("No se ha seleccionado ninguna foto")

        self.boton_guardar = QPushButton("Guardar")
        self.boton_cancelar = QPushButton("Cancelar")

        formulario.addRow("Nombre de usuario:", self.campo_nombre)
        formulario.addRow("Tema:", self.combo_tema)
        formulario.addRow("Idioma:", self.combo_idioma)
        formulario.addRow("Tamaño de fuente:", self.campo_fuente)
        formulario.addRow("Color de barra de menú:", self.boton_color_menu)
        formulario.addRow("Color de letra:", self.boton_color_letra)
        formulario.addRow("Foto de perfil:", self.boton_foto)

        layout_principal.addLayout(formulario)
        layout_principal.addWidget(self.etiqueta_foto)
        layout_principal.addWidget(self.boton_guardar)
        layout_principal.addWidget(self.boton_cancelar)

        self.setLayout(layout_principal)

        self.boton_color_menu.clicked.connect(self.seleccionar_color_menu)
        self.boton_color_letra.clicked.connect(self.seleccionar_color_letra)
        self.boton_foto.clicked.connect(self.seleccionar_foto)
        self.boton_guardar.clicked.connect(self.guardar_datos)
        self.boton_cancelar.clicked.connect(self.reject)

    def cargar_datos(self):
        self.campo_nombre.setText(
            self.configuracion["nombre_usuario"]
        )

        self.combo_tema.setCurrentText(
            self.configuracion["tema_interfaz"]
        )

        self.combo_idioma.setCurrentText(
            self.configuracion["idioma"]
        )

        self.campo_fuente.setValue(
            self.configuracion["tamaño_fuente"]
        )

        self.color_menu = self.configuracion["color_barra_menu"]
        self.color_letra = self.configuracion["color_letra"]
        self.ruta_foto = self.configuracion["foto_perfil"]

        self.actualizar_etiqueta_foto()

    def seleccionar_color_menu(self):
        color = QColorDialog.getColor()

        if color.isValid():
            self.color_menu = color.name()
            self.boton_color_menu.setText(self.color_menu)

    def seleccionar_color_letra(self):
        color = QColorDialog.getColor()

        if color.isValid():
            self.color_letra = color.name()
            self.boton_color_letra.setText(self.color_letra)

    def seleccionar_foto(self):
        ruta, _ = QFileDialog.getOpenFileName(
            self,
            "Seleccionar foto de perfil",
            "",
            "Imágenes (*.png *.jpg *.jpeg *.bmp)"
        )

        if ruta:
            carpeta_imagenes = "images"

            if not os.path.exists(carpeta_imagenes):
                os.makedirs(carpeta_imagenes)

            extension = os.path.splitext(ruta)[1]
            nombre_foto = "perfil" + extension

            ruta_destino = os.path.join(
                carpeta_imagenes,
                nombre_foto
            )

            shutil.copy2(ruta, ruta_destino)

            self.ruta_foto = ruta_destino
            self.actualizar_etiqueta_foto()

    def actualizar_etiqueta_foto(self):
        if self.ruta_foto:
            imagen = QPixmap(self.ruta_foto)

            if not imagen.isNull():
                imagen = imagen.scaled(
                    100,
                    100
                )

                self.etiqueta_foto.setPixmap(imagen)
            else:
                self.etiqueta_foto.setText(
                    "La imagen no pudo cargarse"
                )
        else:
            self.etiqueta_foto.setText(
                "No se ha seleccionado ninguna foto"
            )

    def guardar_datos(self):
        self.configuracion["nombre_usuario"] = (
            self.campo_nombre.text()
        )

        self.configuracion["tema_interfaz"] = (
            self.combo_tema.currentText()
        )

        self.configuracion["idioma"] = (
            self.combo_idioma.currentText()
        )

        self.configuracion["tamaño_fuente"] = (
            self.campo_fuente.value()
        )

        self.configuracion["color_barra_menu"] = self.color_menu
        self.configuracion["color_letra"] = self.color_letra
        self.configuracion["foto_perfil"] = self.ruta_foto

        self.accept()