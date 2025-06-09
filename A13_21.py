class Bank:
    ROI=10.5

    def __init__(self, Name, amount, amt):
        self.Name=Name
        self.amount=amount
        self.amt=amt
        

    def Display(self):
       print("Account customer Name : ", self.Name)
       print("Amount at account: ", self.amount)
       print(" amount after  Withdraw  is:", self.bal)
    
       
       
    def Deposit(self):
         return self.amount
        

    def Withdraw(self):
        self.bal = self.amount-self.amt
        return self.bal

    
    def CalIn(self):
        Interest=(self.bal*self.ROI)/100
        print(f"INterest is:{Interest}")

def main():
    

    N=input("enter the Customer Name:")
   
    A=int(input("enter the amount to deposit at bank:"))

    a=int(input("enter amount to be withdraw:"))
    B1=Bank(N, A,a)
    B1.Deposit()
    B1.Withdraw()
    B1.CalIn()
    B1.Display()

   
if __name__=="__main__":
    main()