import sys
from pathlib import Path

def main():
    if len(sys.argv) != 2:
        print("Usage: python copy_to_demo.py <destination_file>")
        sys.exit(1)

    dest_path = Path(sys.argv[1])

    src_name = input("Enter the name of the existing file to copy from: ")
    src_path = Path(src_name)

    if not src_path.is_file():
        print(f" Source file '{src_path}' does not exist.")
        sys.exit(1)

    with src_path.open("r") as src_file, dest_path.open("w") as dest_file:
        dest_file.write(src_file.read())

    print(f" Copied content from {src_path} to {dest_path}")

if __name__ == "__main__":
    main()
