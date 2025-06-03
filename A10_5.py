from functools import reduce
def checkprime(no):
    if no<1:
        return False
    else:
        for i in range(2, no):
            if(no%i==0):
                return False
        return True

def mul(no):
    for i in range(no):
        ans=no*2

    return ans

def largest(no):
    ret=0
    for i in range(no):
        ret=max(no)

    return ret

n= int(input("enter the no of elements for list:"))
a=[]
for i in range (n):
    values=int(input("elements in the list:"))
    a.append(values)
print("input data:", a)

Fdata=list(filter(checkprime,a))
print("Filter Output:", Fdata)

Mdata=list(map(mul, Fdata))
print("Map Output:", Mdata)

Rdata=reduce(largest, Mdata) 
print("Reduce output", Rdata)
