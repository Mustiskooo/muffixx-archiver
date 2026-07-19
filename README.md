# Muffixx Archiver 🚀

A simple website archiver built with Python.

Muffixx Archiver allows you to save websites locally by downloading the main HTML file and required assets like CSS, JavaScript and images.

## ✨ Features

- 🖥️ Simple GUI interface with Tkinter
- 🌐 Website HTML archiving
- 🎨 CSS file downloading
- ⚙️ JavaScript file downloading
- 🖼️ Image downloading
- 📁 Automatic archive folder creation
- 🕒 Timestamp-based archive naming
- 🛡️ Custom User-Agent and request timeout support

## 📸 Screenshot

_maybe i'll add screenshot here :3_

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/Mustiskooo/muffixx-archiver.git
```

Go to the project folder:

```bash
cd muxfixx-archiver
```

Install requirements:

```bash
pip install -r requirements.txt
```

## ▶️ Usage

Run the application:

```bash
python main.py
```

Enter a website URL and press **Archive**.

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

## 🌐 Viewing Archives

For the best experience, open archives using a local server.

Opening `index.html` directly may cause browser security errors because of `file://` restrictions.

Go into the archive folder:

```bash
cd archives/Your_Archive_Name
```

Start a local server:

```bash
python -m http.server 8000
```

Then open:

```
http://localhost:8000
```

Your archived website will now run through a local web server.

## 🛠️ Technologies

- Python
- Tkinter
- Requests
- BeautifulSoup4

## 📂 Project Structure

```
muffixx-archiver/
│
├── main.py          # GUI application
├── archiver.py      # Website archiving engine
├── config.py        # Configuration settings
├── utils.py         # Utility functions
│
├── archives/        # Generated archives
│
├── requirements.txt
└── README.md
```

## 📌 Version

Current version:

```
v1.0
```

## 👤 Developer

Created by **Mustiskooo**

GitHub:
https://github.com/Mustiskooo

---

⭐ If you like this project, consider giving it a star!
