
def enterlist(no):
    return no

def even(no):
        if no%2==0:
            return no

data=list()
a=int(input("enter number of elements for list:"))
for i in range(a):
    b=int(input("elements in the list are:"))
    enterlist=data.append(b)
    
Fdata=list(filter(enterlist, data)) #filter is inbuilt function
print("Display the list using Filter function", Fdata)

Mdata=list(map(even, Fdata))
print("MAP Function  will give even list is:", Mdata)
