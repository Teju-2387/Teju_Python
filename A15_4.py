import sys
from pathlib import Path
import filecmp

def main():
    if len(sys.argv) != 3:
        print("Usage: python compare_files.py <file1> <file2>")
        sys.exit(1)

    file1, file2 = map(Path, sys.argv[1:])

    for f in (file1, file2):
        if not f.is_file():
            print(f"{f} does not exist or is not a regular file.")
            sys.exit(1)


    are_equal = filecmp.cmp(file1, file2, shallow=False)

    if are_equal:
        print("Success")   # Contents are identical
        sys.exit(0)        # Exit code 0  -> success
    else:
        print("Failure")   # Contents differ
        sys.exit(1)        # Exit code 1  -> failure

if __name__ == "__main__":
    main()
