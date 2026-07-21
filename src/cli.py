import os
import argparse

from archiver import archive_site


BANNER = r"""
 /$$      /$$            /$$$$$$   /$$$$$$  /$$                      /$$$$$$                      /$$       /$$
| $$$    /$$$           /$$__  $$ /$$__  $$|__/                     /$$__  $$                    | $$      |__/
| $$$$  /$$$$ /$$   /$$| $$  \__/| $$  \__/ /$$ /$$   /$$ /$$   /$$| $$  \ $$  /$$$$$$   /$$$$$$$| $$$$$$$  /$$
| $$ $$/$$ $$| $$  | $$| $$$$    | $$$$    | $$|  $$ /$$/|  $$ /$$/| $$$$$$$$ /$$__  $$ /$$_____/| $$__  $$| $$
| $$  $$$| $$| $$  | $$| $$_/    | $$_/    | $$ \  $$$$/  \  $$$$/ | $$__  $$| $$  \__/| $$      | $$  \ $$| $$
| $$\  $ | $$| $$  | $$| $$      | $$      | $$  >$$  $$   >$$  $$ | $$  | $$| $$      | $$      | $$  | $$| $$
| $$ \/  | $$|  $$$$$$/| $$      | $$      | $$ /$$/\  $$ /$$/\  $$| $$  | $$| $$      |  $$$$$$$| $$  | $$| $$
|__/     |__/ \______/ |__/      |__/      |__/|__/  \__/|__/  \__/|__/  |__/|__/       \_______/|__/  |__/|__/

────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
 Author   : Mustiskooo
 Discord  : bnmuffix
 GitHub   : https://github.com/Mustiskooo
 Version  : 1.0
 Platform : Windows | Linux | Termux
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
"""

def get_args():
    parser = argparse.ArgumentParser(
        prog="muffixx-archiver",
        description="Archive websites for offline viewing."
    )

    parser.add_argument(
        "url",
        help="Website URL"
    )

    parser.add_argument(
        "-o",
        "--output",
        default="archives",
        help="Output directory"
    )

    return parser.parse_args()

def main():
    print(BANNER)

    args = get_args()

    print("[*] Configuration")
    print(f" ├─ URL    : {args.url}")
    print(f" └─ Output : {args.output}")
    print()

    print("[*] Starting archive...\n")

    ok, result = archive_site(
        url=args.url,
        output=args.output
    )

    if ok:
        print("\n[+] Archive completed successfully!")
        print(f"[+] Saved to: {result}")
    else:
        print("\n[-] Archive failed!")
        print(f"[-] {result}")


if __name__ == "__main__":
    main()
