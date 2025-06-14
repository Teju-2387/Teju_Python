def print_long_lines(filename: str="Line.txt"):
    print("Enter text for Line.txt (press Enter on a blank line to finish):")
    lines = []
    while True:
        data = input()
        if data == "":
            break
        lines.append(data)

    with open(filename, "w") as f:
        for data in lines:
            f.write(data + "\n")

    with open(filename, "r") as f:
        for lineno, line in enumerate(f, start=1):
            if len(line.split()) > 5:
                print(f"{lineno:>3}: {line.rstrip()}")   # show line number + content

def main():
    file_name = input("Enter the file name: ").strip()
    print_long_lines(file_name)
  
if __name__ == "__main__":
    main()
