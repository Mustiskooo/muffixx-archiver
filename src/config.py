from pathlib import Path

APP_NAME = "Muffixx Archiver"
VERSION = "0.3.0"

BASE_DIR = Path(__file__).resolve().parent

ARCHIVE_DIR = BASE_DIR / "archives"
LOG_DIR = BASE_DIR / "logs"

USER_AGENT = f"{APP_NAME}/{VERSION}"
REQUEST_TIMEOUT = 15

ARCHIVE_DIR.mkdir(exist_ok=True)
LOG_DIR.mkdir(exist_ok=True)
