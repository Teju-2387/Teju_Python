def printstar(n):
    for i in range(1,n+1):
        for j in range(i-1):
            print("*",end= " ")

def main():
    n=int(input("enter a number:"))
    printstar(n)
    
if __name__=="__main__":
    main()