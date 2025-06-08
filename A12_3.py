import math
class Arithmetic:
    
    def __init__(self, V1, V2):
        print("INSIDE INIT Method:")   
        self.Value1= V1
        self.Value2= V2
            
        
    def Add(self):
        Addition=self.Value1+self.Value2
        return  Addition
    
    def Sub(self):
        Subtraction=self.Value1-self.Value2
        return Subtraction
    
    def Mul(self):
        Multiplication=self.Value1*self.Value2
        return Multiplication
    
    def Div(self):
        Division=self.Value1/self.Value2
        return Division
    
def main():
   Value1=int(input("enter first no:"))
   Value2=int(input("enter second no:"))
   A1=Arithmetic(Value1,Value2)
   Addition= A1.Add()
   print(f"The Addition of Two number  is: {Addition}") 
   Subtraction= A1.Sub()
   print(f"Subtraction is: {Subtraction}")
   Multiplication=A1.Mul()
   print(f"Multiplication is: {Multiplication}")
   Division=A1.Div()
   print(f"Divion is: {Division}")
 
if __name__=="__main__":
    main()
    