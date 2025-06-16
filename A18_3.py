import sys
from pathlib import Path
import shutil

NEW_FILE = "new_file.txt"        

def get_multiline_input():
    print("Enter the text you want in", NEW_FILE)
    print("(Press Enter on an empty line to finish.)")
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line + "\n")
    return "".join(lines)

def main():
    if len(sys.argv) != 2:
        print("Usage: python copy_to_existing.py <existing_file>")
        sys.exit(1)

    dest_path = Path(sys.argv[1])

    if not dest_path.exists():
        print(f"{dest_path}' does not exist.")
        sys.exit(1)

    text = get_multiline_input()
    with open(NEW_FILE, "w") as f_new:
        f_new.write(text)

    with open(NEW_FILE, "r") as f_src,open(dest_path, "w") as f_dest:
        shutil.copyfileobj(f_src, f_dest)

    print(f"Copied content from '{NEW_FILE}' to '{dest_path}'.")


if __name__ == "__main__":
    main()
