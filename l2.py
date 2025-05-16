def main():
    return max_num

a=int(input("enter the no of elements for list:"))
data=[] #list  object created

for i in range(a):
    no=int(input("enter the elements for list:"))
    data.append(no)  # add each elemnts into list using no variable
    
if data:
    max_num=data[0]    
    for val in data:   # check each element of the list
        if (val>max_num):
            max_num=val
print("max elements of the list is:", max_num) 

if __name__=="__main__":
    main()