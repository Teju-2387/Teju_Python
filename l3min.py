def main():
    return min_num

a=int(input("enter the no of elemts for the list:"))
data=[]

for i in range(a):
    no=int(input("enter the element for the list:"))
    data.append(no)

if data:
    min_num=data[0]
    for val in data:
        if(val<min_num):
            min_num=val
print("min elements of the list is:", min_num) 

if __name__=="__main__":
    main()