def main():
    return largest
def largest(a,b,c):
    
    if a>=b and a>c:
        print("a is greater",  a)
    elif b>c and b>a:
        print("b is greatest:",b)
    else:
        print("C IS GREATER", c)

v1=int(input("enter the value for V1: "))
v2=int(input("enter the value for v2: "))
v3=int(input("enter the value for v3: "))
result=largest(v1,v2,v3)


if __name__=="__main__":
    main()