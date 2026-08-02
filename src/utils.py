from datetime import datetime
import re

WINDOWS_RESERVED_NAMES = {
    "CON", "PRN", "AUX", "NUL",
    "COM1", "COM2", "COM3", "COM4", "COM5",
    "COM6", "COM7", "COM8", "COM9",
    "LPT1", "LPT2", "LPT3", "LPT4", "LPT5",
    "LPT6", "LPT7", "LPT8", "LPT9",
}


def get_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H-%M-%S")


def sanitize_filename(name):
# Geçersiz karakterleri değiştir
    name = re.sub(r'[<>:"/\\|?*]', "_", name)

# Fazladan boşlukları temizle
    name = re.sub(r"\s+", " ", name).strip()

# Baştaki ve sondaki nokta/boşlukları kaldır
    name = name.strip(" .")

# Yasaklı klasör isimlerini engelle
    if name.upper() in WINDOWS_RESERVED_NAMES:
        name = f"_{name}"

# Çok uzunsa kısalt
    if len(name) > 100:
        name = name[:100].rstrip()

# Boş kaldıysa varsayılan isim kullan
    if not name:
        name = "Archived_Website"

    return name


def format_bytes(size):
    units = ["B", "KB", "MB", "GB", "TB"]

    for unit in units:
        if size < 1024:
            return f"{size:.1f} {unit}"
        size /= 1024

    return f"{size:.1f} PB"