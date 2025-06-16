def main():
    filename = input("Enter the file name (or full path): ")

    with open(filename, "r") as f:
            
            content = f.read()

            print("\n--- File contents ---")
            
            print(content)

if __name__ == "__main__":
    main()
