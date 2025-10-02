# TP2IDS
Este es un respositorio hecho para el TP2 para la materia Introduccion al desarrollo de software  
## Integrantes
- Dylan Ian, Ruiz
- Lucas Nicolas, Luis Roda
- Mariano Ignacio, Molloja Pinto
## Arquitectura del proyecto
El proyecto consta de una aplicacion escrita en Flask para url dinamicas, informacion dinamica, manejo de errores, bloques de codigo para su reutilizacion, para renderizar codigo html, mostrar mensajes con flash y recuperar los datos insertados en el formulario

- Cuenta con Flask-Mail para manejar la logica de enviar mensajes
- Tambien cuenta con python-dotenv para el uso de variables de entorno en la carpeta .env con los datos sensibles para enviar el formulario

## Dependencias
Se necesita:
- Python 3.10 o superior
- Un entorno virtual 
- Dentro del entorno virtual tener instalado Flask, Flask-Mail y python-dotenv

## Como levantar el proyecto
### 1. Crear rutas del archivo y bajar repositorio
- Ejecutamos el script `crear_proyecto.sh`

Esto creara toda la rutas de carpetas a usar

- Desde la carpeta TP2IDS hacer `sudo apt update`

- Luego ejecutar `sudo apt install git`, seguido hacer `git clone "SSHKEY"`, por ultimo desde la branch main `git pull`

Para conseguir la SSH KEY se consigue desde el repositorio publico: https://github.com/marianoignacio/TP2IDS

### 2. Crear y activar entorno virtual con venv
Desde la ruta TP2IDS
- Ejecutas: `python3 -m venv .venv`

Esto creara el entorno virtual en la carpeta oculta `.venv`

Para activarlo:
- Linux: `source .venv/bin/activate`

Para desactivarlo:
- `deactivate`

### 3. Instalar dependencias
Con el entorno virtual previamente activado:
- Ejecutamos: `pip install -r requirements.txt`

Esto instalaria todas las dependencias necesarias para el proyecto

Necesitaras crear un archivo .env con la clave de aplicacion
- Ejecuta: `touch .env` para crera el archivo .env que contendra las variables de entorno
### 4. Correr proyecto
Para correr el proyecto 
- Ejecute: `flask run`

## Features
La pagina cuenta con un navbar con logo, una descripcion del evento, datos relevantes de la carrera, un mapa del recorrido( con los puntos de hidratacion), imagenes del evento y sponsors, kit de la carrera, link al deslinde para firmarlo, pie de pagina con contactos, formulario de inscripcion que se envia a la casilla de mail de la organizacion y pagina auxiliar en caso de error 404