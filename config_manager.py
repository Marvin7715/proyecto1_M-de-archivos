import json
import os

ARCHIVO_CONFIG = "config.json"
ARCHIVO_BACKUP = "config.bak"
ARCHIVO_TEMPORAL = "config.tmp"

CONFIGURACION_DEFAULT = {
    "nombre_usuario": "Usuario",
    "tema_interfaz": "oscuro",
    "idioma": "es-ES",
    "tamaño_fuente": 12,
    "color_barra_menu": "#000000",
    "color_letra": "#FFFFFF",
    "foto_perfil": ""
}

def obtener_configuracion_default():
    return CONFIGURACION_DEFAULT.copy()

def guardar_configuracion(configuracion):
    try:
        if os.path.exists(ARCHIVO_CONFIG):
            with open(ARCHIVO_CONFIG, "r", encoding="utf-8") as archivo:
                contenido_anterior = archivo.read()

            with open(ARCHIVO_BACKUP, "w", encoding="utf-8") as archivo:
                archivo.write(contenido_anterior)

        with open(ARCHIVO_TEMPORAL, "w", encoding="utf-8") as archivo:
            json.dump(
                configuracion,
                archivo,
                indent=4,
                ensure_ascii=False
            )

        os.replace(ARCHIVO_TEMPORAL, ARCHIVO_CONFIG)

        return True

    except PermissionError:
        print("Error: no se tienen permisos para escribir el archivo.")
        return False

    except OSError:
        print("Error: ocurrió un problema al guardar los archivos.")
        return False

def cargar_configuracion():
    if not os.path.exists(ARCHIVO_CONFIG):
        print("El archivo de configuración no existe.")
        print("Se utilizarán los valores predeterminados.")

        return obtener_configuracion_default()

    try:
        with open(ARCHIVO_CONFIG, "r", encoding="utf-8") as archivo:
            configuracion = json.load(archivo)

        if not validar_configuracion(configuracion):
            print("Error: el archivo de configuración tiene un formato inválido.")
            return recuperar_configuracion()

        return configuracion

    except json.JSONDecodeError:
        print("Error: el archivo de configuración está corrupto.")
        return recuperar_configuracion()

    except PermissionError:
        print("Error: no se tienen permisos para leer el archivo.")
        return obtener_configuracion_default()

    except OSError:
        print("Error: ocurrió un problema al leer el archivo.")
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

def recuperar_configuracion():
    if not os.path.exists(ARCHIVO_BACKUP):
        print("No existe un respaldo disponible.")
        print("Se utilizarán los valores predeterminados.")

        return obtener_configuracion_default()

    try:
        with open(ARCHIVO_BACKUP, "r", encoding="utf-8") as archivo:
            configuracion = json.load(archivo)

        if validar_configuracion(configuracion):
            print("Se recuperó la configuración desde el respaldo.")
            return configuracion

        print("El respaldo también tiene un formato inválido.")

    except json.JSONDecodeError:
        print("El archivo de respaldo también está corrupto.")

    except PermissionError:
        print("No se tienen permisos para leer el respaldo.")

    except OSError:
        print("No fue posible leer el respaldo.")

    print("Se utilizarán los valores predeterminados.")
    return obtener_configuracion_default()