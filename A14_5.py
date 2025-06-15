class Bank:
    def __init__(self, acc_no, opening_balance):
        self.acc_no = acc_no
        self.balance = opening_balance

    def withdraw(self, amount):

        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return

        if amount > self.balance:
            print("Insufficient balance: withdrawal denied.")
        else:
            self.balance -= amount
            print(f"₹{amount:,.2f} withdrawn successfully.")


    def display(self):
        print("\n--- Account Details ---")
        print(f"Account No : {self.acc_no}")
        print(f"Balance    : ₹{self.balance:,.2f}")

if __name__ == "__main__":
        acc_input = int(input("Enter account number: "))
        bal_input = float(input("Enter opening balance: "))

        account = Bank(acc_input, bal_input)
        account.display()

        amt_input = float(input("\nEnter amount to withdraw: "))
        account.withdraw(amt_input)

        account.display()
