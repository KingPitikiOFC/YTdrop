YouTube Drop 1.0

YouTube Drop es una herramienta de línea de comandos escrita en Python que permite descargar videos y audios de YouTube de forma rápida y sencilla.

El programa utiliza la biblioteca yt‑dlp y La herramienta externa FFmpeg para la descarga de video y audio en formato MP4 y MP3.
---

Características

- Descarga videos completos de YouTube.
- Descarga audio en formato MP3.
- Barra de progreso en la terminal.
- Spinner de descarga
- Historial automático de descargas.
- Interfaz simple por menú en la terminal.
- Compatible con Python 3.

---

Requisitos

- Python 3.8 o superior
- yt-dlp
- FFmpeg

Instalar dependencia:

pkg update && pkg upgrade
pkg install python -y
pkg install ffmpeg -y
pip install yt-dlp

---

Instalación

1. Clona el repositorio:

git clone https://github.com/KingPitikiOFC/YTdrop.git
2. Entra a la carpeta del proyecto:

cd YTDrop

3. Ejecuta el script:

python yt.py

---

Uso

Al ejecutar el programa verás el menú:

1. Video por URL
2. Audio por URL

Descargar video

1. Selecciona la opción 1
2. Pega la URL del video de YouTube
3. El video se descargará automáticamente

Descargar audio

1. Selecciona la opción 2
2. Pega la URL del video
3. El audio se convertirá a MP3

---

Dónde se guardan las descargas

El programa crea automáticamente estas carpetas:

/sdcard/YouTube/

Dentro de esa carpeta se crean:

/sdcard/YouTube/Audio
/sdcard/YouTube/Video

Videos descargados

/sdcard/YouTube/Video/

Formato:

NombreDelVideo.mp4

Audios descargados

/sdcard/YouTube/Audio/

Formato:

NombreDelVideo.mp3

---

Historial de descargas

Cada descarga se guarda en:

/sdcard/YouTube/history.json

El archivo contiene:

{
    "archivo": "Nombre del video",
    "ruta": "Ruta del archivo",
    "fecha": "YYYY-MM-DD HH:MM:SS"
}

Esto permite llevar un registro de lo que has descargado.

---

Interfaz en consola

El programa muestra:

- Mensajes de información
- Barra de progreso
- Animación de descarga
- Mensajes de éxito o error

Ejemplo:

[INFO] Preparando descarga...
[●●●●●○○○○○○○○○○○○○○○○○○○○○] 45.3%
[ÉXITO] Descarga completada!

---

Estructura del proyecto

YTDrop
│
├── yt.py
└── README.md

---

Autor

Proyecto creado por:

KingPitikiOFC

---

Licencia

Este proyecto es de uso libre para aprendizaje y desarrollo personal.
