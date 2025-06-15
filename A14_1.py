class Emp:

    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def display_details(self):
        print(f"Employee ID   : {self.emp_id}")
        print(f"Employee Name : {self.name}")
        print(f"Salary (₹)    : {self.salary:,.2f}")

if __name__ == "__main__":
        e1 = int(input("Enter employee ID: "))
        e2 = input("Enter employee name: ")
        e3 = float(input("Enter salary: "))

        employee = Emp(e1,e2,e3)

        print("\n--- Employee Details ---")

        employee.display_details()
    