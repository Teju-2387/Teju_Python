class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.__price = price

    def set_price(self, new_price):
        if new_price < 0:
            raise ValueError("Price cannot be negative.")
        self.__price = new_price

    def get_price(self):
        return self.__price

    def display(self):
        print(f"Title : {self.title}")
        print(f"Author: {self.author}")
        print(f"Price : ₹{self.__price:,.2f}")

if __name__ == "__main__":

    book = Book("Python Deep Dive", "Tejaswi Mangave", 599.0)

    print("\nInitial details:")
    book.display()

    book.set_price(649.0)

    print("\nAfter price update (via set_price):")

    book.display()

