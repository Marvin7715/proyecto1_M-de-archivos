import os

from PyQt6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QMessageBox,
    QPushButton,
    QFrame,
    QSizePolicy
)

from PyQt6.QtGui import QPixmap, QPainter, QPainterPath, QFont
from PyQt6.QtCore import Qt

from config_manager import cargar_configuracion, guardar_configuracion
from .settings_window import SettingsWindow


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.configuracion = cargar_configuracion()

        self.setWindowTitle(
            "Config User - Manejo de Archivos"
        )

        self.resize(1100, 700)
        self.setMinimumSize(900, 600)

        self.crear_interfaz()
        self.aplicar_configuracion()
        self.actualizar_datos_usuario()

    def crear_interfaz(self):
        widget_central = QWidget()
        layout_principal = QHBoxLayout()

        layout_principal.setContentsMargins(
            0,
            0,
            0,
            0
        )

        layout_principal.setSpacing(0)

        self.barra_lateral = self.crear_barra_lateral()
        self.panel_principal = self.crear_panel_principal()

        layout_principal.addWidget(
            self.barra_lateral
        )

        layout_principal.addWidget(
            self.panel_principal
        )

        widget_central.setLayout(
            layout_principal
        )

        self.setCentralWidget(
            widget_central
        )

    def crear_barra_lateral(self):
        barra = QFrame()

        barra.setObjectName(
            "barraLateral"
        )

        barra.setFixedWidth(
            230
        )

        layout = QVBoxLayout()

        layout.setContentsMargins(
            20,
            25,
            20,
            20
        )

        layout.setSpacing(
            10
        )

        titulo = QLabel(
            "CONFIG USER"
        )

        titulo.setObjectName(
            "tituloLateral"
        )

        subtitulo = QLabel(
            "Gestión de configuración"
        )

        subtitulo.setObjectName(
            "subtituloLateral"
        )

        boton_inicio = QPushButton(
            "Inicio"
        )

        boton_settings = QPushButton(
            "Settings"
        )

        boton_archivo = QPushButton(
            "Archivo"
        )

        boton_edicion = QPushButton(
            "Edición"
        )

        boton_ver = QPushButton(
            "Ver"
        )

        boton_inicio.clicked.connect(
            self.mostrar_inicio
        )

        boton_settings.clicked.connect(
            self.abrir_settings
        )

        boton_archivo.clicked.connect(
            self.opcion_no_disponible
        )

        boton_edicion.clicked.connect(
            self.opcion_no_disponible
        )

        boton_ver.clicked.connect(
            self.opcion_no_disponible
        )

        layout.addWidget(
            titulo
        )

        layout.addWidget(
            subtitulo
        )

        layout.addSpacing(
            25
        )

        layout.addWidget(
            boton_inicio
        )

        layout.addWidget(
            boton_settings
        )

        layout.addWidget(
            boton_archivo
        )

        layout.addWidget(
            boton_edicion
        )

        layout.addWidget(
            boton_ver
        )

        layout.addStretch()

        estado = QLabel(
            "Sistema de configuración"
        )

        estado.setObjectName(
            "estadoLateral"
        )

        layout.addWidget(
            estado
        )

        barra.setLayout(
            layout
        )

        return barra

    def crear_panel_principal(self):
        panel = QFrame()

        panel.setObjectName(
            "panelPrincipal"
        )

        layout = QVBoxLayout()

        layout.setContentsMargins(
            45,
            35,
            45,
            35
        )

        layout.setSpacing(
            20
        )

        encabezado = QHBoxLayout()

        self.titulo_principal = QLabel(
            "Bienvenido"
        )

        self.titulo_principal.setObjectName(
            "tituloPrincipal"
        )

        self.estado = QLabel(
            "Configuración cargada"
        )

        self.estado.setObjectName(
            "estadoPrincipal"
        )

        encabezado.addWidget(
            self.titulo_principal
        )

        encabezado.addStretch()

        encabezado.addWidget(
            self.estado
        )

        layout.addLayout(
            encabezado
        )

        self.subtitulo_principal = QLabel(
            "Administra las preferencias de tu aplicación."
        )

        self.subtitulo_principal.setObjectName(
            "subtituloPrincipal"
        )

        layout.addWidget(
            self.subtitulo_principal
        )

        tarjeta_usuario = QFrame()

        tarjeta_usuario.setObjectName(
            "tarjetaUsuario"
        )

        layout_usuario = QVBoxLayout()

        layout_usuario.setContentsMargins(
            30,
            30,
            30,
            30
        )

        self.foto_perfil = QLabel()

        self.foto_perfil.setFixedSize(
            180,
            180
        )

        self.foto_perfil.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        self.foto_perfil.setObjectName(
            "fotoPerfil"
        )

        self.nombre_usuario = QLabel(
            "Usuario"
        )

        self.nombre_usuario.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        self.nombre_usuario.setObjectName(
            "nombreUsuario"
        )

        layout_usuario.addWidget(
            self.foto_perfil,
            alignment=Qt.AlignmentFlag.AlignCenter
        )

        layout_usuario.addWidget(
            self.nombre_usuario
        )

        tarjeta_usuario.setLayout(
            layout_usuario
        )

        layout.addWidget(
            tarjeta_usuario
        )

        tarjeta_configuracion = QFrame()

        tarjeta_configuracion.setObjectName(
            "tarjetaConfiguracion"
        )

        layout_configuracion = QVBoxLayout()

        titulo_configuracion = QLabel(
            "Configuración actual"
        )

        titulo_configuracion.setObjectName(
            "tituloTarjeta"
        )

        self.dato_tema = QLabel()
        self.dato_idioma = QLabel()
        self.dato_fuente = QLabel()

        layout_configuracion.addWidget(
            titulo_configuracion
        )

        layout_configuracion.addWidget(
            self.dato_tema
        )

        layout_configuracion.addWidget(
            self.dato_idioma
        )

        layout_configuracion.addWidget(
            self.dato_fuente
        )

        tarjeta_configuracion.setLayout(
            layout_configuracion
        )

        layout.addWidget(
            tarjeta_configuracion
        )

        self.boton_editar = QPushButton(
            "Editar configuración"
        )

        self.boton_editar.setObjectName(
            "botonPrincipal"
        )

        self.boton_editar.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Fixed
        )

        self.boton_editar.clicked.connect(
            self.abrir_settings
        )

        layout.addWidget(
            self.boton_editar
        )

        layout.addStretch()

        panel.setLayout(
            layout
        )

        return panel

    def aplicar_configuracion(self):
        tema = self.configuracion[
            "tema_interfaz"
        ]

        tamaño_fuente = self.configuracion[
            "tamaño_fuente"
        ]

        color_menu = self.configuracion[
            "color_barra_menu"
        ]

        color_letra = self.configuracion[
            "color_letra"
        ]

        fuente = QFont(
            "Segoe UI",
            tamaño_fuente
        )

        self.setFont(
            fuente
        )

        if tema == "oscuro":
            fondo = "#181A1F"
            tarjeta = "#292D34"
            texto_secundario = "#B8BCC5"
            borde = "#383D46"
            entrada = "#30343C"
        else:
            fondo = "#F4F6F8"
            tarjeta = "#FFFFFF"
            texto_secundario = "#626975"
            borde = "#DDE1E6"
            entrada = "#F7F8FA"

        self.setStyleSheet(
            f"""
            QMainWindow {{
                background-color: {fondo};
            }}

            QWidget {{
                font-family: 'Segoe UI';
            }}

            #barraLateral {{
                background-color: {color_menu};
            }}

            #tituloLateral {{
                color: {color_letra};
                font-size: 24px;
                font-weight: bold;
            }}

            #subtituloLateral {{
                color: {color_letra};
                font-size: 11px;
            }}

            #estadoLateral {{
                color: {color_letra};
                font-size: 11px;
            }}

            #panelPrincipal {{
                background-color: {fondo};
            }}

            #tituloPrincipal {{
                color: {color_letra};
                font-size: 28px;
                font-weight: bold;
            }}

            #subtituloPrincipal {{
                color: {texto_secundario};
                font-size: 14px;
            }}

            #estadoPrincipal {{
                color: {color_letra};
                background-color: {entrada};
                border: 1px solid {borde};
                border-radius: 10px;
                padding: 8px 14px;
            }}

            #tarjetaUsuario,
            #tarjetaConfiguracion {{
                background-color: {tarjeta};
                border: 1px solid {borde};
                border-radius: 16px;
            }}

            #fotoPerfil {{
                background-color: {entrada};
                border: 3px solid {borde};
                border-radius: 90px;
            }}

            #nombreUsuario {{
                color: {color_letra};
                font-size: 22px;
                font-weight: bold;
                padding-top: 10px;
            }}

            #tituloTarjeta {{
                color: {color_letra};
                font-size: 18px;
                font-weight: bold;
            }}

            #tarjetaConfiguracion QLabel {{
                color: {texto_secundario};
                font-size: 14px;
                padding: 3px;
            }}

            QPushButton {{
                background-color: {entrada};
                color: {color_letra};
                border: 1px solid {borde};
                border-radius: 8px;
                padding: 10px;
                font-size: {tamaño_fuente}px;
                text-align: left;
            }}

            QPushButton:hover {{
                border: 1px solid {color_letra};
            }}

            #botonPrincipal {{
                background-color: {color_menu};
                color: {color_letra};
                border: none;
                border-radius: 10px;
                padding: 14px;
                text-align: center;
                font-weight: bold;
            }}

            #botonPrincipal:hover {{
                background-color: {entrada};
            }}
            """
        )

    def actualizar_datos_usuario(self):
        nombre = self.configuracion[
            "nombre_usuario"
        ]

        tema = self.configuracion[
            "tema_interfaz"
        ]

        idioma = self.configuracion[
            "idioma"
        ]

        tamaño = self.configuracion[
            "tamaño_fuente"
        ]

        self.titulo_principal.setText(
            f"Bienvenido, {nombre}"
        )

        self.nombre_usuario.setText(
            nombre
        )

        self.dato_tema.setText(
            f"Tema: {tema}"
        )

        self.dato_idioma.setText(
            f"Idioma: {idioma}"
        )

        self.dato_fuente.setText(
            f"Tamaño de fuente: {tamaño}px"
        )

        self.aplicar_foto_perfil()

    def crear_foto_circular(self, ruta):
        imagen_original = QPixmap(
            ruta
        )

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
            160,
            160,
            Qt.AspectRatioMode.IgnoreAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )

        resultado = QPixmap(
            160,
            160
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
            160,
            160
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

    def aplicar_foto_perfil(self):
        ruta_foto = self.configuracion[
            "foto_perfil"
        ]

        if ruta_foto and os.path.exists(
            ruta_foto
        ):
            imagen = self.crear_foto_circular(
                ruta_foto
            )

            if not imagen.isNull():
                self.foto_perfil.setPixmap(
                    imagen
                )

                return

        self.foto_perfil.clear()

        self.foto_perfil.setText(
            "Sin foto"
        )

    def mostrar_inicio(self):
        self.actualizar_datos_usuario()

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
            self.configuracion = (
                ventana_settings.configuracion
            )

            if guardar_configuracion(
                self.configuracion
            ):
                self.aplicar_configuracion()
                self.actualizar_datos_usuario()

                self.estado.setText(
                    "Configuración guardada"
                )

                QMessageBox.information(
                    self,
                    "Configuración",
                    "La configuración se guardó correctamente."
                )

            else:
                self.estado.setText(
                    "Error al guardar"
                )

                QMessageBox.critical(
                    self,
                    "Error",
                    "No fue posible guardar la configuración."
                )