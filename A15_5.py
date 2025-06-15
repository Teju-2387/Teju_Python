def main():

    filename = input("Enter the file name: ")
    target   = input("Enter the string to search for: ")

    with open(filename, "r") as f:
            content = f.read()

            if target in content:
                  
                  print("Success")   # The string was found
            else:
                 print("Failure")   # The string was not found

if __name__ == "__main__":
    main()
