
class Emp:
    def __init__(self, name, department, salary):
        
        self.name = name

        self._department = department

        self.__salary = salary

    
    def get_salary(self):
        return self.__salary

   
    def display(self):
        print(f"Name       : {self.name}")          # public
        print(f"Department : {self._department}")  # protected
        print(f"Salary     : ₹{self.__salary}")  # private
    
    
    if __name__ == "__main__":
        e1=input("enter Name:")
        e2=input("enter Department Name:")
        e3=int(input("enter salary:"))

        emp = Emp(e1,e2,e3)

        print("\n--- Using display() ---")
        emp.display()
  
        print("\n--- Direct attribute access ---")
 
        print("emp.name", emp.name)


        print("emp._department", emp._department)

        print(emp.__salary)

        print("emp.get_salary()    ->", emp.get_salary())

        emp.set_salary(70000)
    
