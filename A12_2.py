import math
class circle:
    PI=3.14  #class variable

    def __init__(self, R):
        print("INSIDE INIT Method:")   
        self.Radius= R
             
    
    def Calarea(self):
        Area=self.PI*self.Radius**2
        return  Area
    
    def Calcirum(self):
        Circum=2*self.PI*self.Radius
        return Circum
    
def main():
  r=int(input("enter a value for Radius:")) 
  c1=circle(r)
  Circum = c1.Calcirum()
  print(f"The circumference of the circle is: {Circum:.2f}") 
  Area = c1.Calarea()
  print(f"Area of a circle is:{Area:.2f}")

if __name__=="__main__":
    main()
    