from functools import reduce

def prime(n):
        if n==1 or n==0:
             return False
        elif n>1:
             for i in range(2, n+1):
                  if(n%i==0):
                       return n

data=list()
a=int(input("enter a no of elements:"))
for i in range(a):
    b=int(input("list elements are:"))
    enterlist=data.append(b)

print("List Input Is:", data)


Fdata=list(filter(prime, data))
print("enter list using filter:", Fdata)
