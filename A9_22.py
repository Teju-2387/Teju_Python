def main():
    
    ans =lambda x, y : x*y
    
    no1=int(input("enter number 1:"))
    no2=int(input("enter number 2:"))

    print(f"multiplication  of given {no1} and {no2} is: {ans(no1, no2)}")

if __name__=="__main__":
    main()