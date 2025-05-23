from functools import reduce

def mul(i, no):
    for i in range(no):
        product= i*no
        return product

data=list()
a=int(input("enter a no of elements:"))
for i in range(a):
    b=int(input("list elements are:"))
    enterlist=data.append(b)

print("LIST ITEM ARE:", data)

Rdata=list(reduce(mul, data))
print("using reduce function list value get:", Rdata)
