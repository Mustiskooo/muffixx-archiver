from cli import get_args
from archiver import archive_site


def main():
    args = get_args()

    ok, result = archive_site(
        url=args.url,
        output=args.output
    )

    if ok:
        print(f"\n✅ Archive created successfully!")
        print(f"📁 {result}")
    else:
        print(f"\n❌ Error:")
        print(result)


if __name__ == "__main__":
    main()
