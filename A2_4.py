def factsum(n):
    sum=0
    for i in range(1, n+1):
        if n%i==0:
            sum=sum+i
    return sum    
    
def main():
    a=int(input("enter a number to calcluate factors of a number:"))
    result=factsum(a)
    print("sum of factor of a given number is:",result)

if __name__=="__main__":
    main()
    