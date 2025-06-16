import os
from pathlib import Path

def main():
    filename = input("Enter the file name (or full path): ")

    file_path = Path(filename)
    if file_path.exists():
        print(f"The file '{file_path}' exists.")
    else:
        print(f"The file '{file_path}' does NOT exist.")


if __name__ == "__main__":
    main()
