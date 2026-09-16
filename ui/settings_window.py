import os
import shutil

from PyQt6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QHBoxLayout,
    QFormLayout,
    QLineEdit,
    QComboBox,
    QSpinBox,
    QPushButton,
    QColorDialog,
    QFileDialog,
    QLabel,
    QMessageBox,
    QFrame
)

from PyQt6.QtGui import QPixmap, QPainter, QPainterPath
from PyQt6.QtCore import Qt


class SettingsWindow(QDialog):

    def __init__(self, configuracion, parent=None):
        super().__init__(parent)

        self.configuracion = configuracion.copy()

        self.color_menu = self.configuracion[
            "color_barra_menu"
        ]

        self.color_letra = self.configuracion[
            "color_letra"
        ]

        self.ruta_foto = self.configuracion[
            "foto_perfil"
        ]

        self.setWindowTitle(
            "Settings - Configuración de Usuario"
        )

        self.setFixedSize(
            650,
            650
        )

        self.crear_interfaz()
        self.cargar_datos()
        self.aplicar_estilo()

    def crear_interfaz(self):
        layout_principal = QVBoxLayout()

        layout_principal.setContentsMargins(
            30,
            25,
            30,
            25
        )

        layout_principal.setSpacing(
            18
        )

        titulo = QLabel(
            "Configuración de usuario"
        )

        titulo.setObjectName(
            "titulo"
        )

        subtitulo = QLabel(
            "Personaliza la apariencia y preferencias de la aplicación."
        )

        subtitulo.setObjectName(
            "subtitulo"
        )

        layout_principal.addWidget(
            titulo
        )

        layout_principal.addWidget(
            subtitulo
        )

        tarjeta_perfil = QFrame()

        tarjeta_perfil.setObjectName(
            "tarjeta"
        )

        layout_perfil = QHBoxLayout()

        layout_perfil.setContentsMargins(
            20,
            20,
            20,
            20
        )

        self.etiqueta_foto = QLabel(
            "Sin foto"
        )

        self.etiqueta_foto.setFixedSize(
            110,
            110
        )

        self.etiqueta_foto.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        self.etiqueta_foto.setObjectName(
            "foto"
        )

        self.boton_foto = QPushButton(
            "Seleccionar foto"
        )

        self.boton_foto.clicked.connect(
            self.seleccionar_foto
        )

        layout_foto = QVBoxLayout()

        layout_foto.addStretch()

        layout_foto.addWidget(
            self.boton_foto
        )

        layout_foto.addStretch()

        layout_perfil.addWidget(
            self.etiqueta_foto
        )

        layout_perfil.addLayout(
            layout_foto
        )

        tarjeta_perfil.setLayout(
            layout_perfil
        )

        layout_principal.addWidget(
            tarjeta_perfil
        )

        tarjeta_configuracion = QFrame()

        tarjeta_configuracion.setObjectName(
            "tarjeta"
        )

        formulario = QFormLayout()

        formulario.setContentsMargins(
            20,
            20,
            20,
            20
        )

        formulario.setSpacing(
            14
        )

        self.campo_nombre = QLineEdit()

        self.combo_tema = QComboBox()

        self.combo_tema.addItems(
            [
                "claro",
                "oscuro"
            ]
        )

        self.combo_idioma = QComboBox()

        self.combo_idioma.addItems(
            [
                "es",
                "es-ES",
                "en",
                "en-US"
            ]
        )

        self.campo_fuente = QSpinBox()

        self.campo_fuente.setMinimum(
            8
        )

        self.campo_fuente.setMaximum(
            48
        )

        self.boton_color_menu = QPushButton(
            "Seleccionar color"
        )

        self.boton_color_letra = QPushButton(
            "Seleccionar color"
        )

        formulario.addRow(
            "Nombre de usuario:",
            self.campo_nombre
        )

        formulario.addRow(
            "Tema:",
            self.combo_tema
        )

        formulario.addRow(
            "Idioma:",
            self.combo_idioma
        )

        formulario.addRow(
            "Tamaño de fuente:",
            self.campo_fuente
        )

        formulario.addRow(
            "Color de barra:",
            self.boton_color_menu
        )

        formulario.addRow(
            "Color de letra:",
            self.boton_color_letra
        )

        tarjeta_configuracion.setLayout(
            formulario
        )

        layout_principal.addWidget(
            tarjeta_configuracion
        )

        layout_botones = QHBoxLayout()

        self.boton_cancelar = QPushButton(
            "Cancelar"
        )

        self.boton_guardar = QPushButton(
            "Guardar cambios"
        )

        self.boton_guardar.setObjectName(
            "botonGuardar"
        )

        self.boton_cancelar.clicked.connect(
            self.reject
        )

        self.boton_guardar.clicked.connect(
            self.guardar_datos
        )

        layout_botones.addStretch()

        layout_botones.addWidget(
            self.boton_cancelar
        )

        layout_botones.addWidget(
            self.boton_guardar
        )

        layout_principal.addLayout(
            layout_botones
        )

        self.setLayout(
            layout_principal
        )

        self.boton_color_menu.clicked.connect(
            self.seleccionar_color_menu
        )

        self.boton_color_letra.clicked.connect(
            self.seleccionar_color_letra
        )

        self.combo_tema.currentTextChanged.connect(
            self.cambiar_tema
        )

    def cargar_datos(self):
        self.campo_nombre.setText(
            self.configuracion[
                "nombre_usuario"
            ]
        )

        self.combo_tema.setCurrentText(
            self.configuracion[
                "tema_interfaz"
            ]
        )

        self.combo_idioma.setCurrentText(
            self.configuracion[
                "idioma"
            ]
        )

        self.campo_fuente.setValue(
            self.configuracion[
                "tamaño_fuente"
            ]
        )

        self.actualizar_boton_color(
            self.boton_color_menu,
            self.color_menu
        )

        self.actualizar_boton_color(
            self.boton_color_letra,
            self.color_letra
        )

        self.actualizar_foto()

    def cambiar_tema(self):
        self.aplicar_estilo()

    def seleccionar_color_menu(self):
        color = QColorDialog.getColor(
            parent=self
        )

        if color.isValid():
            self.color_menu = color.name()

            self.actualizar_boton_color(
                self.boton_color_menu,
                self.color_menu
            )

    def seleccionar_color_letra(self):
        color = QColorDialog.getColor(
            parent=self
        )

        if color.isValid():
            self.color_letra = color.name()

            self.actualizar_boton_color(
                self.boton_color_letra,
                self.color_letra
            )

    def actualizar_boton_color(
        self,
        boton,
        color
    ):
        boton.setText(
            color
        )

        boton.setStyleSheet(
            f"""
            QPushButton {{
                background-color: {color};
                border: 1px solid #888888;
                border-radius: 7px;
                padding: 8px;
                color: white;
                font-weight: bold;
            }}
            """
        )

    def seleccionar_foto(self):
        ruta, _ = QFileDialog.getOpenFileName(
            self,
            "Seleccionar foto de perfil",
            "",
            "Imágenes (*.png *.jpg *.jpeg *.bmp)"
        )

        if ruta:
            carpeta_imagenes = "images"

            if not os.path.exists(
                carpeta_imagenes
            ):
                os.makedirs(
                    carpeta_imagenes
                )

            extension = os.path.splitext(
                ruta
            )[1]

            nombre_foto = (
                "perfil" + extension
            )

            ruta_destino = os.path.join(
                carpeta_imagenes,
                nombre_foto
            )

            try:
                shutil.copy2(
                    ruta,
                    ruta_destino
                )

                self.ruta_foto = (
                    ruta_destino
                )

                self.actualizar_foto()

            except OSError:
                QMessageBox.critical(
                    self,
                    "Error",
                    "No fue posible copiar la imagen."
                )

    def actualizar_foto(self):
        if self.ruta_foto and os.path.exists(
                self.ruta_foto
        ):
            imagen = self.crear_foto_circular(
                self.ruta_foto
            )

            if not imagen.isNull():
                self.etiqueta_foto.setPixmap(
                    imagen
                )

                return

        self.etiqueta_foto.clear()

        self.etiqueta_foto.setText(
            "Sin foto"
        )

    def guardar_datos(self):
        nombre = self.campo_nombre.text().strip()

        if not nombre:
            QMessageBox.warning(
                self,
                "Dato requerido",
                "El nombre de usuario no puede estar vacío."
            )

            return

        self.configuracion[
            "nombre_usuario"
        ] = nombre

        self.configuracion[
            "tema_interfaz"
        ] = self.combo_tema.currentText()

        self.configuracion[
            "idioma"
        ] = self.combo_idioma.currentText()

        self.configuracion[
            "tamaño_fuente"
        ] = self.campo_fuente.value()

        self.configuracion[
            "color_barra_menu"
        ] = self.color_menu

        self.configuracion[
            "color_letra"
        ] = self.color_letra

        self.configuracion[
            "foto_perfil"
        ] = self.ruta_foto

        self.accept()

    def aplicar_estilo(self):
        tema = self.combo_tema.currentText()

        if tema == "oscuro":
            fondo = "#181A1F"
            tarjeta = "#22252B"
            entrada = "#30343C"
            borde = "#3B404A"
            texto = "#F2F3F5"
            secundario = "#B8BCC5"
            texto_combo = "#FFFFFF"
        else:
            fondo = "#F4F6F8"
            tarjeta = "#FFFFFF"
            entrada = "#FFFFFF"
            borde = "#CDD2D8"
            texto = "#20242A"
            secundario = "#68707C"
            texto_combo = "#20242A"

        self.setStyleSheet(
            f"""
            QDialog {{
                background-color: {fondo};
            }}

            QLabel {{
                color: {texto};
            }}

            #titulo {{
                color: {texto};
                font-size: 26px;
                font-weight: bold;
            }}

            #subtitulo {{
                color: {secundario};
                font-size: 13px;
            }}

            #tarjeta {{
                background-color: {tarjeta};
                border: 1px solid {borde};
                border-radius: 14px;
            }}

            #foto {{
                background-color: {entrada};
                border: 3px solid {borde};
                border-radius: 55px;
            }}

            QLineEdit,
            QComboBox,
            QSpinBox {{
                background-color: {entrada};
                color: {texto};
                border: 1px solid {borde};
                border-radius: 7px;
                padding: 8px;
            }}

            QLineEdit:focus,
            QComboBox:focus,
            QSpinBox:focus {{
                border: 1px solid {self.color_menu};
            }}

            QComboBox {{
                selection-background-color: {self.color_menu};
                selection-color: {texto_combo};
            }}

            QComboBox QAbstractItemView {{
                background-color: {tarjeta};
                color: {texto};
                border: 1px solid {borde};
                selection-background-color: {self.color_menu};
                selection-color: {texto_combo};
                padding: 4px;
            }}

            QComboBox QAbstractItemView::item {{
                padding: 8px;
            }}

            QSpinBox {{
                selection-background-color: {self.color_menu};
                selection-color: {texto_combo};
            }}

            QPushButton {{
                background-color: {entrada};
                color: {texto};
                border: 1px solid {borde};
                border-radius: 7px;
                padding: 9px 14px;
            }}

            QPushButton:hover {{
                border: 1px solid {self.color_menu};
            }}

            #botonGuardar {{
                background-color: {self.color_menu};
                color: {self.color_letra};
                border: none;
                font-weight: bold;
                padding: 10px 18px;
            }}

            #botonGuardar:hover {{
                opacity: 0.9;
            }}
            """
        )

    def crear_foto_circular(self, ruta):
        imagen_original = QPixmap(ruta)

        if imagen_original.isNull():
            return QPixmap()

        tamaño = min(
            imagen_original.width(),
            imagen_original.height()
        )

        x = (
            imagen_original.width() - tamaño
        ) // 2

        y = (
            imagen_original.height() - tamaño
        ) // 2

        imagen = imagen_original.copy(
            x,
            y,
            tamaño,
            tamaño
        )

        imagen = imagen.scaled(
            100,
            100,
            Qt.AspectRatioMode.IgnoreAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )

        resultado = QPixmap(
            100,
            100
        )

        resultado.fill(
            Qt.GlobalColor.transparent
        )

        pintor = QPainter(
            resultado
        )

        pintor.setRenderHint(
            QPainter.RenderHint.Antialiasing
        )

        ruta_circular = QPainterPath()

        ruta_circular.addEllipse(
            0,
            0,
            100,
            100
        )

        pintor.setClipPath(
            ruta_circular
        )

        pintor.drawPixmap(
            0,
            0,
            imagen
        )

        pintor.end()

        return resultado