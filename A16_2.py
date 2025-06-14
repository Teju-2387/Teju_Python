import os
def main():
    print("enter the name of file you want to create:")

    Filename=input()

    fobj= open(Filename, "w")

    fobj.write("Pallavi Teju  Sushma Bina Ramesh")

    fobj=open(Filename,"r")

    content=fobj.read()

    while(content!=""):
        print(content)

    fobj.close()
if __name__=="__main__":
    main()