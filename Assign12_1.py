class demo:
    value="AISSMS"  #class variable

    def __init__(self, no1, no2):
        print("INSIDE INIT Method:")   
        self.Name = no1
        self.Salary = no2
        

    def __del__(self):
        print("Inside Destrcutor:")

    def fun(self):       #instance method1
        print("Inside Instance Method:")
        print("number 1:", self.Name)
        print("number 2:", self.Salary)
    
    def gun(self):         #instance method2
        print("Inside Instance Method:")
        print("number 1:", self.Name)
        print("number 2:", self.Salary)


def main():
    print("Class variable : "+demo.value)
    obj1=demo(11,21)
    obj2=demo(101,501)
    obj1.fun()
    obj2.fun()

    obj1.gun()
    obj2.gun()

if __name__=="__main__":
    main()
    