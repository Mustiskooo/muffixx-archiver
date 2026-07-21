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
    url = input("[?] Website URL: ").strip()

    output = input("[?] Output Folder [archives]: ").strip()
    if not output:
        output = "archives"

    class Args:
        pass

    args = Args()
    args.url = url
    args.output = output

    return args
 
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
