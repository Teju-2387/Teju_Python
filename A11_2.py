def factorial(n):
    fact=1
    for i in range(1,n+1):  #logic
        fact=fact*i          #logic
    print("factorial of a given numbers are:", fact)  #output

def main():
    n=int(input("enter a number:"))  #input
    factorial(n)   #recursive call

    print()
    

if __name__=="__main__":
    main()
