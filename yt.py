#!/usr/bin/env python3
# KingPitiki OFC - YOUTUBE DOWNLOADER

import os
import sys
import threading
import time
import json
from datetime import datetime
import yt_dlp

MAINTENANCE_MODE = True
MAINTENANCE_REASON = "Actualizando sistema de descargas"

if MAINTENANCE_MODE:
    print(f"""
╔══════════════════════════════╗
║        ⛔MANTENIMIENTO⛔      ║
╚══════════════════════════════╝

YTdrop está temporalmente en mantenimiento.
Motivo: {MAINTENANCE_REASON}

Intenta nuevamente más tarde.

— KingPitikiOFC
""")
    sys.exit()
# ==============================

# Directorios de almacenamiento
AUDIO_DIR = "/sdcard/YouTube/Audio"
VIDEO_DIR = "/sdcard/YouTube/Video"
HISTORY_DIR = "/sdcard/YouTube"
HISTORY_FILE = os.path.join(HISTORY_DIR, "history.json")

os.makedirs(AUDIO_DIR, exist_ok=True)
os.makedirs(VIDEO_DIR, exist_ok=True)
os.makedirs(HISTORY_DIR, exist_ok=True)

# Colores para consola
class C:
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    RED = "\033[91m"
    YELLOW = "\033[93m"
    CYAN = "\033[96m"
    END = "\033[0m"
    BOLD = "\033[1m"

# Función de logging
def log(msg, tipo="INFO"):
    colores = {
        "INFO": C.BLUE,
        "ÉXITO": C.GREEN,
        "ERROR": C.RED,
        "ADVERTENCIA": C.YELLOW
    }
    color = colores.get(tipo, C.BLUE)
    print(f"{color}[{tipo}] {datetime.now().strftime('%H:%M:%S')} - {msg}{C.END}")

# Banner inicial
def banner():
    print(f"""{C.BOLD}{C.CYAN}
╔══════════════════════════════╗
║      YOUTUBE DROP  1.0       ║
╚══════════════════════════════╝
Creador KingPitikiOFC
{C.END}""")

# Guardar historial
def guardar_historial(nombre, ruta):
    data = []
    if os.path.exists(HISTORY_FILE):
        try:
            with open(HISTORY_FILE, "r") as f:
                data = json.load(f)
        except:
            data = []

    data.append({
        "archivo": nombre,
        "ruta": ruta,
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    })

    with open(HISTORY_FILE, "w") as f:
        json.dump(data, f, indent=4)

# Spinner animado
spinner_activo = False
t = None
def spinner():
    global spinner_activo
    anim = "|/-\\"
    i = 0
    while spinner_activo:
        sys.stdout.write(f"\r{C.CYAN}Descargando video {anim[i % len(anim)]}{C.END}")
        sys.stdout.flush()
        time.sleep(0.1)
        i += 1
    sys.stdout.write("\r" + " " * 40 + "\r")
    sys.stdout.flush()

# Barra de progreso
def barra_progreso(d):
    global spinner_activo, t
    if d["status"] == "downloading":
        if spinner_activo and t:
            spinner_activo = False
            t.join()
        total = d.get("total_bytes") or d.get("total_bytes_estimate")
        descargado = d.get("downloaded_bytes", 0)
        if not total:
            return
        porcentaje = descargado / total
        barra = 25
        llenos = int(barra * porcentaje)
        vacios = barra - llenos
        bar = "●" * llenos + "○" * vacios
        sys.stdout.write(f"\r{C.YELLOW}[{bar}] {porcentaje*100:5.1f}%{C.END}")
        sys.stdout.flush()
    elif d["status"] == "finished":
        print()

# Descargar video
def descargar_video(url):
    global spinner_activo, t
    log("Preparando descarga...", "INFO")
    spinner_activo = True
    t = threading.Thread(target=spinner)
    t.start()
    ydl_opts = {
        "format": "bestvideo*+bestaudio/best",
        "merge_output_format": "mp4",
        "outtmpl": os.path.join(VIDEO_DIR, "%(title)s.%(ext)s"),
        "quiet": True,
        "no_warnings": True,
        "noprogress": True,
        "progress_hooks": [barra_progreso],
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            ruta = ydl.prepare_filename(info)
            spinner_activo = False
            t.join()
            guardar_historial(info["title"], ruta)
            log("Descarga completada!", "ÉXITO")
    except Exception as e:
        spinner_activo = False
        t.join()
        log(f"{e}", "ERROR")

# Descargar audio
def descargar_audio(url):
    log("Preparando descarga de audio...", "INFO")
    ydl_opts = {
        "format": "bestaudio",
        "outtmpl": os.path.join(AUDIO_DIR, "%(title)s.%(ext)s"),
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
        "quiet": True,
        "no_warnings": True,
        "noprogress": True,
        "progress_hooks": [barra_progreso],
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            ruta = os.path.join(AUDIO_DIR, f"{info['title']}.mp3")
            guardar_historial(info["title"], ruta)
            log("Descarga completada!", "ÉXITO")
    except Exception as e:
        log(f"{e}", "ERROR")

# Menú principal
def menu():
    banner()
    print(f"""{C.YELLOW}

1. Video por URL
2. Audio por URL

{C.END}""")
    op = input(f"{C.CYAN}Selecciona la opción > {C.END}").strip()
    if op == "1":
        url = input(f"{C.CYAN}URL video > {C.END}").strip()
        descargar_video(url)
    elif op == "2":
        url = input(f"{C.CYAN}URL audio > {C.END}").strip()
        descargar_audio(url)
    else:
        log("Opción inválida", "ERROR")

if __name__ == "__main__":
    menu()