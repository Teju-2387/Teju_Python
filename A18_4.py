#!/usr/bin/env python3
import sys
from pathlib import Path

def read_file(path: Path):
    with open(path, "rb") as f:
        return f.read()
    
def main():
    if len(sys.argv) != 3:
        print(" Usage: python compare_files.py <file1> <file2>")
        sys.exit(1)

    file1, file2 = Path(sys.argv[1]), Path(sys.argv[2])

    for p in (file1, file2):
        if not p.exists():
            print(f" '{p}' does not exist.")
            sys.exit(1)

        if read_file(file1) == read_file(file2):
            print("SUCCESS")   
        else:
            print("FAILURE")  

if __name__ == "__main__":
    main()
