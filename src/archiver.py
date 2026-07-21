from pathlib import Path
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

from config import (
    USER_AGENT,
    REQUEST_TIMEOUT
)

from utils import (
    sanitize_filename,
    get_timestamp
)


def download_file(url, folder):
    try:
        r = requests.get(
            url,
            timeout=REQUEST_TIMEOUT,
            headers={
                "User-Agent": USER_AGENT
            }
        )

        r.raise_for_status()

        filename = url.split("/")[-1].split("?")[0]

        if not filename:
            filename = "file"

        filename = sanitize_filename(filename)

        path = folder / filename

        with open(path, "wb") as f:
            f.write(r.content)

        return filename

    except Exception:
        return None


def archive_site(url, output="archives"):
    try:
        response = requests.get(
            url,
            timeout=REQUEST_TIMEOUT,
            headers={
                "User-Agent": USER_AGENT
            }
        )

        response.raise_for_status()

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        title = (
            soup.title.string.strip()
            if soup.title and soup.title.string
            else "website"
        )

        folder_name = (
            sanitize_filename(title)
            + "_"
            + get_timestamp()
        )

        output_dir = Path(output)
        output_dir.mkdir(parents=True, exist_ok=True)

        archive_path = output_dir / folder_name
        archive_path.mkdir(parents=True, exist_ok=True)

        assets = archive_path / "assets"

        css_dir = assets / "css"
        js_dir = assets / "js"
        img_dir = assets / "img"

        css_dir.mkdir(parents=True, exist_ok=True)
        js_dir.mkdir(parents=True, exist_ok=True)
        img_dir.mkdir(parents=True, exist_ok=True)

        # CSS
        for link in soup.find_all("link"):
            href = link.get("href")

            if href and "stylesheet" in link.get("rel", []):
                css_url = urljoin(url, href)

                filename = download_file(css_url, css_dir)

                if filename:
                    link["href"] = f"assets/css/{filename}"

        # JavaScript
        for script in soup.find_all("script"):
            src = script.get("src")

            if src:
                js_url = urljoin(url, src)

                filename = download_file(js_url, js_dir)

                if filename:
                    script["src"] = f"assets/js/{filename}"

        # Images
        for img in soup.find_all("img"):
            src = img.get("src")

            if src:
                img_url = urljoin(url, src)

                filename = download_file(img_url, img_dir)

                if filename:
                    img["src"] = f"assets/img/{filename}"

        with open(
            archive_path / "index.html",
            "w",
            encoding="utf-8"
        ) as f:
            f.write(str(soup))

        return True, archive_path

    except Exception as e:
        return False, str(e)
