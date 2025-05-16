def main():
    return sum
a=int(input("enter the no of elements for list:"))
data=[]

for i in range(a):
    no=int(input("enter the elements for list:"))
    data.append(no)
    sum=0
    
for value in data:
    sum+=value
    
print("sum of list  elements are:", sum) 

if __name__=="__main__":
    main()