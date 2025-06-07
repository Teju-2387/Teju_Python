def countnum(n):
    count=0
    for digit in str(n):
        if digit=='0':
            count=count+1
    print("number of zeros in the given digit is:", count)    

def main():
    n=int(input("enter a number:")) 
    countnum(n)
    
if __name__=="__main__":
    main()