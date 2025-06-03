from functools import reduce

n= int(input("enter the no of elements for list:"))
a=[]
for i in range (n):
    values=int(input("elements in the list:"))
    a.append(values)

Fdata=list(filter(lambda no: no%2==0, a))
print("Filter Output:", Fdata)

Mdata=list(map(lambda no: no**2, Fdata))
print("Map Output:", Mdata)

Rdata=reduce(lambda A,B: A+B, Mdata)
print("Reduce output", Rdata)