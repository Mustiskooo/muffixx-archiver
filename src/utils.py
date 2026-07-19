from datetime import datetime
import re

def get_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def sanitize_filename(name):
    return re.sub(r'[<>:"/\\|?*]', "_", name)


def format_bytes(size):
    units = ["B", "KB", "MB", "GB", "TB"]

    for unit in units:
        if size < 1024:
            return f"{size:.1f} {unit}"
        size /= 1024

    return f"{size:.1f} PB"
