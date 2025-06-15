from pathlib import Path
def main():
    filename = input("Enter the file name: ").strip()

    file_path = Path(filename)        

    if file_path.is_file():            
        print(f"'{filename}' exists at: {file_path.resolve()}")
    else:
        print(f"'{filename}' does NOT exist in the current directory.")

if __name__ == "__main__":
    main()
