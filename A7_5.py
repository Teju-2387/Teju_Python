def main():
    rev=" "
    str=input("enter a string :")
    for char in str:
        rev=char+rev
    if str==rev:
        print("String is  Palindrome")
    else:
        print("string is not Palindrome")
if __name__=="__main__":
    main()