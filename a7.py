def main():
    return Area, Peri

def Area(a,b):
    area= a*b
    return area


def Peri(a,b):
    peri=2*(a+b)
    return peri


l=int(input("enter the length of the rectangle: "))
bradth=int(input("enter the breadth of the rectangle: "))


result=Area(l, bradth)
result1=Peri(l,bradth)

print("area if rectangle is:" , result)

print("perimeter of rectangle is:", result1)


if __name__=="__main__":
    main()