class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price


    def equal(self, other: "Product"):
        if not isinstance(other, Product):
            return NotImplemented
        return self.price == other.price
    
    def __repr__(self):
        return (f"Product({self.name!r}, ₹{self.price:.2f}")
    
if __name__ == "__main__":
    p1 = Product("Laptop:", 49_999)
    p2 = Product("Phone", 49_999)
    p3 = Product("Headphones", 2_999)

    print("--- Product objects ---")
    print(p1)
    print(p2)
    print(p3)

    print("\n--- Using equal() method ---")
    print(f"p1.equal(p2): {p1.equal(p2)}")  
    print(f"p1.equal(p3): {p1.equal(p3)}")  
