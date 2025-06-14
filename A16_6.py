def stu(filename="student.txt"):
    n = int(input("How many students? "))
    with open(filename, "w") as f:
        for i in range(n):
            name  = input(f"Enter name of student {i+1}: ").strip()
            marks = int(input(f"Enter marks for {name}: "))
            f.write(f"{name},{marks}\n")       

def show(filename="student.txt", threshold=75):
    print(f"\nStudents scoring above {threshold}:")
    with open(filename, "r") as f:
        for line in f:
            if not line.strip():         
                continue
            name, marks = line.strip().split(",")
            if int(marks) > threshold:
                print(name)

if __name__ == "__main__":
    stu()  
    show()
