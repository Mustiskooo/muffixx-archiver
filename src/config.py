from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

ARCHIVE_DIR = BASE_DIR / "archives"
LOG_DIR = BASE_DIR / "logs"

ARCHIVE_DIR.mkdir(exist_ok=True)
LOG_DIR.mkdir(exist_ok=True)