def main():
    square=lambda x:x**2
    cube=lambda y: y**3
    a=int(input("enter a number to calculate square and cube"))
    r1=square(a)
    print("Square is :", r1)
    r2=cube(a)
    print("cube is:", r2)
if __name__=="__main__":
    main()
    
