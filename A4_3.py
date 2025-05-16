from functools import reduce
def min_max(no):
    if(no>=70 and no<=90):
        return min_max
        

def increase(no):
    return no+10

#def mul(A,B):
    #return A*B

Data=int(input("enter the number of  elemnts"))
for i in range(Data):
    a=[]
    Values=int(input("enter the elements"))
a.append(Values)


print("Input Data", a)

Fdata=list(filter(min_max, a))
print("Filter Output", Fdata)

Mdata=list(map(increase, Fdata))
print("Map Output", Mdata)

#Rdata=reduce(mul, Mdata)
#print("Reduce output", Rdata)