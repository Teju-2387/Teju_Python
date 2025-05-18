def fact(n):
    if n<0:
        return "not exist"
    elif n==0 or n==1:
         return 1
    else:
         return n*fact(n-1)    
    
def main():
     n=0
     a=int(input("enter the number:"))
     result=fact(a)
     print("factorial of a number is:", result)

if __name__=="__main__":
     main()

    
