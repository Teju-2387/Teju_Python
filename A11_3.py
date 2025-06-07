def sumoffirstnatural(n):
    sum=0
    for i in range(1,n+1):  #logic
        sum =sum+i

    print("sum  of numbers is:", sum)  #output

def main():
    n=int(input("enter a number:"))  #input
    sumoffirstnatural(n)   #recursive call

    print()
    

if __name__=="__main__":
    main()
