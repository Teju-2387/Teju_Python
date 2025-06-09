class Bookstore:
    NoofBooks=0

    def __init__(self, Name, Author):
        self.Name=Name
        self.Author=Author
        Bookstore.NoofBooks=self.NoofBooks+1
        
    def Display(self):
       print("Inside Display Method:")
       print("Book  Name : ", self.Name)
       print("Author Name : ", self.Author)
       print("no of Books:", self.NoofBooks)

def main():
   
    Name=input("enter the Book Name:")
    Author=input("enter the Author Name:")

    B1=Bookstore(Name,Author)
    B1.Display()
   
   
if __name__=="__main__":
    main()