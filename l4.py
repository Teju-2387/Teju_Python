def main():
    return val

a=int(input("enter the no of elemts for the list:"))
data=[]

for i in range(a):
    no=int(input("enter the element for the list:"))
    data.append(no)
    counted=[]

for val in range(len(data)):
        if data[val] not in counted:
             count=0
             for val1 in range(len(data)):
                  if data[val]==data[val1]:
                       count+=1
             counted.append(val)
print("min elements of the list is:", val) 

if __name__=="__main__":
    main()