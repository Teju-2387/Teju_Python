def isprime(n):
    for i in range(2, n+1):
        if n%i==0:
            return "not a prime"
        else:
            return "Prime"
    
def main():
    a=int(input("enter a number to calcluate  a prime number:"))
    result=isprime(a)
    print(" a given number is:",result)

if __name__=="__main__":
    main()
    