# 🎬 YouTube Drop

Herramienta de línea de comandos escrita en **Python** para descargar **videos y audios de YouTube** de forma rápida y sencilla.

Utiliza **yt-dlp** para la descarga y **FFmpeg** para la conversión a **MP4** y **MP3**.

---

## ✨ Características

- Descarga videos completos de YouTube
- Descarga audio en formato **MP3**
- Barra de progreso en la terminal
- Animación **spinner** durante la descarga
- Historial automático de descargas
- Interfaz simple por menú
- Compatible con **Python 3**

---

## ⚙️ Requisitos

- Python **3.8+**
- **yt-dlp**
- **FFmpeg**

---

## 📦 Instalación (Termux)

```bash
pkg update && pkg upgrade
pkg install python -y
pkg install ffmpeg -y
pip install yt-dlp
```

---

## 🚀 Instalación del proyecto

```bash
git clone https://github.com/KingPitikiOFC/YTdrop.git
cd YTdrop
python yt.py
```

---

## 📥 Uso

Al ejecutar el programa aparecerá el menú:

```
1) Descargar video por URL
2) Descargar audio por URL
3) Salir
```

### Descargar video

1. Selecciona **1**
2. Pega la URL del video
3. El video se descargará automáticamente

Formato:

```
NombreDelVideo.mp4
```

---

### Descargar audio

1. Selecciona **2**
2. Pega la URL del video
3. El audio se convertirá a **MP3**

Formato:

```
NombreDelVideo.mp3
```

---

## 📁 Ubicación de descargas

El programa crea automáticamente:

```
/sdcard/YouTube/
```

Dentro se generan las carpetas:

```
/sdcard/YouTube/Video/
/sdcard/YouTube/Audio/
```

---

## 🧾 Historial de descargas

Cada descarga se guarda en:

```
/sdcard/YouTube/history.json
```

Ejemplo:

```json
{
 "archivo": "Nombre del video",
 "ruta": "Ruta del archivo",
 "fecha": "YYYY-MM-DD HH:MM:SS"
}
```

---

## 🖥️ Interfaz en consola

Ejemplo:

```
[INFO] Preparando descarga...
[██████████░░░░░░░░░░] 45.3%
[ÉXITO] Descarga completada
```

---

## 📂 Estructura del proyecto

```
YTDrop
├── yt.py
└── README.md
```

---

## 👨‍💻 Autor

**KingPitikiOFC**

---

## 📜 Licencia

Proyecto de uso libre para **aprendizaje y desarrollo personal**.

El autor **no se hace responsable del uso indebido del software**.