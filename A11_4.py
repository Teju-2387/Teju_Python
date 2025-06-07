def powernum(base, exp):
    if exp==0:
        return 1
    else:
        return base*powernum(base,exp-1)
    

def main():
    base=int(input("enter a base number:")) 
    exp=int(input("enter a  exponent number:"))
   
    result=powernum(base, exp)   #recursive call

    print("Result is", result)
    

if __name__=="__main__":
    main()
