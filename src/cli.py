import argparse

def get_args():
    parser = argparse.ArgumentParser(
        prog="muffixx-archiver",
        description="Archive websites for offline viewing."
    )

    parser.add_argument(
        "url",
        help="Website URL to archive"
    )

    parser.add_argument(
        "-o", "--output",
        default="archives",
        help="Output directory"
    )

    parser.add_argument(
        "-d", "--depth",
        type=int,
        default=1,
        help="Crawl depth (default: 1)"
    )

    parser.add_argument(
        "--no-css",
        action="store_true",
        help="Don't download CSS files"
    )

    parser.add_argument(
        "--no-js",
        action="store_true",
        help="Don't download JavaScript files"
    )

    parser.add_argument(
        "--no-images",
        action="store_true",
        help="Don't download images"
    )

    parser.add_argument(
        "-q", "--quiet",
        action="store_true",
        help="Silent mode"
    )

    return parser.parse_args()
