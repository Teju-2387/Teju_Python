class Rectangle:

    def __init__(self, length: float, width: float) -> None:
        self.length = length
        self.width = width

    
    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def display(self):
        print(f"Length    : {self.length}")
        print(f"Width     : {self.width}")
        print(f"Area      : {self.area():.2f}")
        print(f"Perimeter : {self.perimeter():.2f}")

if __name__ == "__main__":
        length_val = float(input("Enter the rectangle's length: "))
        width_val = float(input("Enter the rectangle's width : "))


        rect = Rectangle(length_val, width_val)
        print("\n--- Rectangle Details ---")
        rect.display()
    
