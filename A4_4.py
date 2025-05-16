from functools import reduce

def Checkeven(no):
    return  no%2==0 

def increase(no):
    return no**2

def add(A, B):
    return A+B

Data=int(input("enter the number of  elemnts"))
for i in range(Data):
    a=[]
    Values=int(input("enter the elements"))
a.append(Values)


Fdata=list(filter(Checkeven, a)) #filter is inbuilt function
print("Filter Output", Fdata)

Mdata=list(map(increase, Fdata))
print("Map Output", Mdata)

Rdata=list(reduce(add, Mdata))
print("Reduce output", Rdata)