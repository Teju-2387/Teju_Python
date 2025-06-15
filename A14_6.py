class Calculator:

    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

    
    def add(self):
        return self.n1 + self.n2
    
    def sub(self):
        return self.n1 - self.n2
    
    def mul(self):
        return self.n1 * self.n2
    
    def div(self):
        return self.n1/self.n2
    

    def display(self):
        print(f"Number 1   : {self.n1}")
        print(f"Number 2 : {self.n2}")
        print(f"Addition is     : {self.add():.2f}")
        print(f"Subtraction is: {self.sub():.2f}")
        print(f"Mul is     : {self.mul():.2f}")
        print(f"Division is     : {self.div():.2f}")

if __name__ == "__main__":
        V1= float(input("Enter the Number 1: "))
        V2 = float(input("Enter the number 2 : "))


        Cal = Calculator(V1, V2)
        print("\n--- Airthmatic  Details ---")
        Cal.display()
    
