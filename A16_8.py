def create_file(filename="blank.txt"):
    print(f"Enter text for {filename}:")
    with open(filename, "w") as f:
        while True:
            line = input()
            if line == "":          # empty line → stop input loop
                break
            f.write(line + "\n")
    print(f"{filename} saved\n")

def remove_blank_lines(src="blank.txt", dst="clean.txt"):
    removed = 0
    with open(src, "r") as fsrc, open(dst, "w") as fdst:
        for line in fsrc:
            if line.strip():        # keep only non‑blank lines
                fdst.write(line)
            else:
                removed += 1
    print(f"Copied cleaned content to '{dst}' ({removed}")


if __name__ == "__main__":
    create_file()          
    remove_blank_lines() 
