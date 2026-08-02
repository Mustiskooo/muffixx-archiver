# Muffixx Archiver 🚀

A simple website archiver built with Python.

Muffixx Archiver allows you to save websites locally by downloading the main HTML file and required assets like CSS, JavaScript and images.

## ✨ Features

- Simple CLI interface
- Website HTML archiving
- CSS file downloading
- JavaScript file downloading
- Archive folder creation
- Timestamp-based archive folder naming

## 📸 Screenshots

_i'll add screenshot here soon :3_

## 📦 Installation

Clone the repository:

```
git clone https://github.com/Mustiskooo/muffixx-archiver.git
```

Go to the project folder:

```
cd muffixx-archiver
```

Install requirements:

```bash
pip install -r requirements.txt
```

## Usage

Run the application:

```bash
python main.py
```

Enter a website URL and press **Enter**.

The archived website will be saved inside:

```
archives/
```

Example:

```
archives/
└── GitHub_Profile_2026-07-19_13-52-52/
    ├── index.html
    └── assets/
        ├── css/
        ├── js/
        └── img/
```

## ❗ IMPORTANT

For the best experience, open archives using a local server.

Opening `index.html` directly may cause browser security errors because of `file://` restrictions.

Go into the archive folder:

```
cd archives/[ARCHIVE NAME]
```

Start a local server:

```
python -m http.server 8000
```

Then open:

```
http://localhost:8000
```

Your archived website will now run through a local web server.

## 🛠️ Technologies

- Python
- requests
- beautifulsoup4

## 📂 Project Structure

```
muffixx-archiver
    │   .gitkeep
    │   README.md
    │
    └───src
        │   .gitkeep
        │   archiver.py
        │   cli.py
        │   config.py
        │   main.py
        │   run.bat
        │   utils.py
        │
        ├───archives
        ├───logs
        └───__pycache__ [Auto-generated on first run]


```

## 📌 Version

Current version is **v1.0**

## Planned Features

- Support for more asset types (fonts, videos, icons, etc.)
- Better error handling
- Bug fixes and performance improvements

## 🐞 Issues / Requests

Found a bug or have an idea for a new feature?

Feel free to open an issue or send me an email at [muffixx@proton.me](mailto:muffixx@proton.me).

I'll do my best to fix bugs and implement new features whenever I have time.
    
## 👤 Developer

Created by **Mustiskooo**

**Built with <3 with Python**

GitHub:
https://github.com/Mustiskooo

---

⭐ If you like this project, consider giving it a star!
