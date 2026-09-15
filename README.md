# Proyecto 1 — Manejo e Implementación de Archivos

## Aplicación de Escritorio con Gestión de Configuración de Usuario

Aplicación desarrollada en Python utilizando PyQt6 para implementar una interfaz gráfica de escritorio y un sistema de gestión de configuración de usuario mediante archivos JSON.

## Descripción

El proyecto permite visualizar y modificar diferentes parámetros de configuración del usuario desde una ventana de Settings.

La aplicación permite configurar:

* Nombre de usuario.
* Tema de interfaz claro u oscuro.
* Idioma.
* Tamaño de fuente.
* Color de la barra de menú.
* Color de letra.
* Foto de perfil.

La configuración se almacena en un archivo JSON y se recupera automáticamente al iniciar la aplicación.

## Tecnologías utilizadas

* Python
* PyQt6
* JSON
* Git y GitHub

## Estructura del proyecto

```text
Proyecto_Archivos/
│
├── main.py
├── config_manager.py
├── config.json
├── .gitignore
│
├── ui/
│   ├── __init__.py
│   ├── main_window.py
│   └── settings_window.py
│
├── images/
│   └── perfil.jpg
│   └── perfil.png
│
├── ejemplos/
│   └── config.bak
│
└── evidencias/
    ├── archivo_ausente.png
    ├── archivo_corrupto.png
    ├── formato_invalido.png
    └── sin_permisos.png
```

## Persistencia de datos

La aplicación utiliza JSON como formato de almacenamiento de la configuración.

El archivo principal utilizado es:

```text
config.json
```

La aplicación también utiliza:

```text
config.bak
```

como respaldo de la configuración anterior y:

```text
config.tmp
```

como archivo temporal durante el proceso de guardado seguro.

El archivo temporal no forma parte de los archivos permanentes del proyecto.

## Escritura segura

Antes de reemplazar la configuración actual, la aplicación conserva una copia de la configuración anterior y posteriormente escribe la nueva configuración en un archivo temporal.

El flujo implementado es:

```text
config.json
     ↓
config.bak
     ↓
config.tmp
     ↓
reemplazo de config.json
```

Esto evita sobrescribir directamente el archivo original durante el proceso de escritura.

## Manejo de errores

La aplicación contempla los siguientes casos:

* Archivo de configuración inexistente.
* Archivo JSON corrupto.
* Archivo JSON con estructura inválida.
* Falta de permisos de lectura o escritura.

Cuando ocurre un problema, la aplicación utiliza un comportamiento controlado y evita finalizar mediante un error no controlado.

## Codificación

La lectura y escritura de los archivos se realiza utilizando UTF-8, permitiendo conservar correctamente caracteres como tildes y `ñ`.

## Ejecución

### 1. Instalar Python

Se requiere Python instalado en el sistema.

### 2. Instalar PyQt6

Desde la terminal:

```bash
pip install PyQt6
```

### 3. Ejecutar la aplicación

Desde la carpeta principal del proyecto:

```bash
python main.py
```

## Evidencias

La carpeta `evidencias` contiene las capturas realizadas durante las pruebas de:

* Archivo ausente.
* Archivo corrupto.
* Formato inválido.
* Falta de permisos.

## Autor

Marvin Vásquez
Ingeniería en Informática y Sistemas