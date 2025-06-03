from functools import reduce

x=lambda no: no%2==0
y=lambda no: no**2
z=lambda A,B: A+B

n= int(input("enter the no of elements for list:"))
a=[]
for i in range (n):
    values=int(input("elements in the list:"))
    a.append(values)


Fdata=list(filter(x,a))
print("Filter Output:", Fdata)

Mdata=list(map(y, Fdata))
print("Map Output:", Mdata)

Rdata=reduce(z, Mdata) 
print("Reduce output", Rdata)
