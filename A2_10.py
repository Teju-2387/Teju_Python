def addsum(n):
    sum=0
    for i in range(1, n):
        sum=sum+n%10
        n=n//10
    return sum
    
def main():
    a=int(input("enter a number to calcluate sum of its digits:"))
    result=addsum(a)
    print("sum of its digits  is:",result)

if __name__=="__main__":
    main()
    