def main():
    return evenodd
def evenodd(a):
    
    if a%2==0:
        print("a is even number",  a)
    else:
        print("a is odd number", a)

v1=int(input("enter the value for V1: "))
result=evenodd(v1)


if __name__=="__main__":
    main()