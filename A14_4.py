class Stu:
    School_Name="YCHP"
    def __init__(self, roll_no, S_name):
        self.roll_no = roll_no
        self.S_name = S_name
    

    def display_details(self):
        print(f"Student Roll No  : {self.roll_no}")
        print(f"Student Name : {self.S_name}")
        print(f"School name   : {self.School_Name}")

if __name__ == "__main__":
        S1 = int(input("Enter Student Roll No: "))
        S2 = input("Enter Student  name: ")
        S3 = input("Enter school Name: ")

        St= Stu(S1,S2)

        print("\n--- Employee Details ---")

        St.display_details()
    