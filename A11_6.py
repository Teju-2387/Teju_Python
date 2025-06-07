def sumofnum(n):
    sum=0
    for i in range(1,n+1):
            sum=sum+n%10
            n=n//10       
    print("sum of digit in  the given number is:", sum)

def main():
    n=int(input("enter a number:")) 
    sumofnum(n)

    
if __name__=="__main__":
    main()