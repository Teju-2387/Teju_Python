def write_source(filename="source.txt"):
    
    print(f"Enter text to store in {filename} (blank line to finish):")
    with open(filename, "w") as f:
        while True:
            line = input()
            if line == "":          # blank line → stop
                break
            f.write(line + "\n")
    print(f"\nSaved your content to {filename}\n")


def copy_file(src="source.txt", dst="destination.txt"):
    with open(src, "r") as fsrc, open(dst, "w") as fdst:
        for line in fsrc:
            fdst.write(line)
    print(f"Copied content from '{src}'to '{dst}'\n")


if __name__ == "__main__":
    write_source()          # Step 1: create & fill source.txt
    copy_file()             # Step 2: duplicate into destination.txt
    