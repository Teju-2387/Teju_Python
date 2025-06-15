from pathlib import Path

def main():
    filename = input("Enter the file name: ").strip()
    file_path = Path(filename)

    if not file_path.is_file():
        print(f" '{filename}' does NOT exist or is not a regular file.")
        return

    with file_path.open("r") as f:
            content = f.read()
            print("\n--- File Contents ---")
            print(content)
            print("--- End of File ---")

if __name__ == "__main__":
    main()
