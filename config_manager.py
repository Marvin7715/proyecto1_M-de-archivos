import json
import os

ARCHIVO_CONFIG = "config.json"
ARCHIVO_BACKUP = "config.bak"
ARCHIVO_TEMPORAL = "config.tmp"

CONFIGURACION_DEFAULT = {
    "nombre_usuario": "Usuario",
    "tema_interfaz": "claro",
    "idioma": "es-ES",
    "tamaño_fuente": 12,
    "color_barra_menu": "#E6B325",
    "color_letra": "#000000",
    "foto_perfil": ""
}

def obtener_configuracion_default():
    return CONFIGURACION_DEFAULT.copy()

def guardar_configuracion(configuracion):
    try:
        with open(ARCHIVO_CONFIG, "w", encoding="utf-8") as archivo:
            json.dump(
                configuracion,
                archivo,
                indent=4,
                ensure_ascii=False
            )

        return True

    except PermissionError:
        print("Error: no se tienen permisos para escribir el archivo.")
        return False

    except OSError:
        print("Error: ocurrió un problema al guardar el archivo.")
        return False

def cargar_configuracion():
    if not os.path.exists(ARCHIVO_CONFIG):
        print("El archivo de configuración no existe.")
        print("Se utilizarán los valores predeterminados.")

        configuracion = obtener_configuracion_default()
        guardar_configuracion(configuracion)

        return configuracion

    try:
        with open(ARCHIVO_CONFIG, "r", encoding="utf-8") as archivo:
            configuracion = json.load(archivo)

        if not validar_configuracion(configuracion):
            print("Error: el archivo de configuración tiene un formato inválido.")
            print("Se utilizarán los valores predeterminados.")

            return obtener_configuracion_default()

        return configuracion

    except json.JSONDecodeError:
        print("Error: el archivo de configuración está corrupto.")
        print("Se utilizarán los valores predeterminados.")

        return obtener_configuracion_default()

    except PermissionError:
        print("Error: no se tienen permisos para leer el archivo.")
        print("Se utilizarán los valores predeterminados.")

        return obtener_configuracion_default()

    except OSError:
        print("Error: ocurrió un problema al leer el archivo.")
        print("Se utilizarán los valores predeterminados.")

        return obtener_configuracion_default()


def validar_configuracion(configuracion):
    campos_requeridos = [
        "nombre_usuario",
        "tema_interfaz",
        "idioma",
        "tamaño_fuente",
        "color_barra_menu",
        "color_letra",
        "foto_perfil"
    ]

    for campo in campos_requeridos:
        if campo not in configuracion:
            return False

    if not isinstance(configuracion["nombre_usuario"], str):
        return False

    if configuracion["tema_interfaz"] not in ["claro", "oscuro"]:
        return False

    if configuracion["idioma"] not in ["es", "es-ES", "en", "en-US"]:
        return False

    if not isinstance(configuracion["tamaño_fuente"], int):
        return False

    if not isinstance(configuracion["color_barra_menu"], str):
        return False

    if not isinstance(configuracion["color_letra"], str):
        return False

    if not isinstance(configuracion["foto_perfil"], str):
        return False

    return True