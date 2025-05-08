def Add(a,b):
    c=a+b
    return c
def main():
    print("enter value1")
    v1=int(input())
    print("enter value2")
    v2=int(input())
    ans=Add(v1,v2)
    print("addition of Two numbers is:", ans)
if __name__=="__main__":
    main()
    