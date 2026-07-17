import requests
from bs4 import BeautifulSoup
from datetime import datetime
from pathlib import Path
from urllib.parse import urljoin

from config import ARCHIVE_DIR


def download_file(url, folder):
    try:
        r = requests.get(
            url,
            timeout=15,
            headers={
                "User-Agent": "MuffixxArchiver/0.2"
            }
        )

        r.raise_for_status()

        filename = url.split("/")[-1].split("?")[0]

        if not filename:
            filename = "file"

        path = folder / filename

        with open(path, "wb") as f:
            f.write(r.content)

        return filename

    except:
        return None


def archive_site(url):
    try:
        response = requests.get(
            url,
            timeout=15,
            headers={
                "User-Agent": "MuffixxArchiver/0.2"
            }
        )

        response.raise_for_status()

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        title = (
            soup.title.string
            if soup.title
            else "website"
        )

        folder_name = (
            title
            .replace("/", "_")
            .replace("\\", "_")
            + "_"
            + datetime.now().strftime("%Y-%m-%d_%H-%M")
        )


        archive_path = ARCHIVE_DIR / folder_name
        archive_path.mkdir()


        assets = archive_path / "assets"
        css_dir = assets / "css"
        js_dir = assets / "js"
        img_dir = assets / "img"


        css_dir.mkdir(parents=True)
        js_dir.mkdir()
        img_dir.mkdir()


        # CSS
        for link in soup.find_all("link"):
            href = link.get("href")

            if href and "stylesheet" in link.get("rel", []):
                css_url = urljoin(url, href)
                download_file(css_url, css_dir)


        # JS
        for script in soup.find_all("script"):
            src = script.get("src")

            if src:
                js_url = urljoin(url, src)
                download_file(js_url, js_dir)


        # Images
        for img in soup.find_all("img"):
            src = img.get("src")

            if src:
                img_url = urljoin(url, src)
                download_file(img_url, img_dir)


        with open(
            archive_path / "index.html",
            "w",
            encoding="utf-8"
        ) as f:
            f.write(str(soup))


        return True, archive_path


    except Exception as e:
        return False, str(e)