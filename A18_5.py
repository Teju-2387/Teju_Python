def main():
    file_name = input("Enter the file name: ")
    search_str = input("Enter the string to search for: ")
    with open(file_name, "r", encoding="utf-8") as f:
            text = f.read().lower()
            
    frequency = text.count(search_str)

    print(f"The string '{search_str}' occurs {frequency} time(s) in '{file_name}'.")

if __name__ == "__main__":
    main()
