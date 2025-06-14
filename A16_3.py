def write_content(filename: str = "demo.txt"):

    print("Enter text for demo.txt (press Enter on a blank line to finish):")
    lines = []
    while True:
        data = input()
        if data == "":
            break
        lines.append(data)


    with open(filename, "w") as f:
        for data in lines:
            f.write(data + "\n")


def file_stats(filename: str = "demo.txt"):
    
    line_count = word_count = char_count = 0

    with open(filename, "r") as f:
        for data in f:
            line_count += 1
            word_count += len(data.split())   # split on any whitespace
            char_count += len(data)           # includes newline char

    return line_count, word_count, char_count


def main():
    write_content("demo.txt")                         # 1️⃣ create & write
    lines, words, chars = file_stats("demo.txt")      # 2️⃣ measure
    print("\n===== demo.txt statistics =====")
    print(f"Lines      : {lines}")
    print(f"Words      : {words}")
    print(f"Characters : {chars}")


if __name__ == "__main__":
    main()
