def main():
    return Add, Sub, Mul, Div
def Add(a,b):
    c=a+b
    return c
v1=int(input("enter value for v1:"))
v2=int(input("enter value for v2:"))

result=Add(v1,v2)
print("Addition is", result)

def Sub(a,b):
    c=a-b
    return c
result=Sub(v1,v2)
print("Subtraction is", result)


def Mul(a,b):
    c=a*b
    return c
result=Mul(v1,v2)
print("Multiplication is", result)

def Div(a,b):
    c=a/b
    return c
result=Div(v1,v2)
print("Division is", result)


if __name__=="__main__":
    main()