class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        print(f"Name : {self.name}")
        print(f"Age  : {self.age}")


class Teacher(Person):

    def __init__(self, name, age, subject, salary):
        super().__init__(name, age)          # call the base‑class constructor
        self.subject = subject
        self.salary = salary

    def display_teacher(self):

        self.display_person()
        
        print(f"Subject : {self.subject}")
        print(f"Salary  : ₹{self.salary}")

if __name__ == "__main__":
    n1=input("enter name of a teacher:")
    n2=input("enter the age of Teacher:")
    n3=input("enter the subject name:")
    n4=float(input("enter the salary of a teacher:"))
    
   

    t = Teacher(n1,n2, n3, n4)

    print("--- Teacher Details ---")

    t.display_teacher()
