def digitscount(n):
        
        return len(str(n))
    
def main():
    a=int(input("enter a number to calcluate number of its digits:"))
    result=digitscount(a)
    print("count of  digits  is:",result)

if __name__=="__main__":
    main()
    