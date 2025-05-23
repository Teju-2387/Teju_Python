from functools import reduce
def enterlist(no):
    return enterlist

def increase(no):
    return no*2

data=list()
a=int(input("enter number of elements for list:"))
for i in range(a):
    b=int(input("elements in the list are:"))
    enterlist=data.append(b)
    
Fdata=list(filter(enterlist, data)) #filter is inbuilt function
print("Display the list using Filter function", Fdata)

Mdata=list(map(increase, Fdata))
print("MAP Function  will Double the list is:", Mdata)
