# Week-05/Task01.py
# Task 1: Define a class for a bank account with attributes for
# account number, balance, and owner name. Include methods for
# deposit, withdrawal, and transfer.
print ("=== TASK #1 OUTPUT ===")

class Bank_Account:
    def __init__(self, owner_name, account_no, balance, ):
        self.owner_name = owner_name
        self.account_no = account_no
        self.balance = balance
        
    def check_balance(self):
         print(f"{self.owner_name}'s Current Balance: {self.balance}")

    def deposit(self, amount):
        self.balance += amount
        print("Amount was deposited Successfully!")
        print("Deposted Amount:", amount)
        print("Total balance:", self.balance)

    def withdrawal(self, amount):
        if amount <= self.balance:
           self.balance -= amount
           print("Amount Withdrawn Successfully!")
           print("Rs.", amount, "was withdrawn")
           print("Total balance:", self.balance)
        else:
            print("Insufficient balance")

    def transfer(self, target_account, amount):
        if amount <= self.balance:
            self.balance -= amount
            target_account.balance += amount
            print("Transfered Amount:", amount)
            print(self.owner_name,"New Balance:", self.balance)
            print(target_account.owner_name,"New Balance: ",target_account.balance)
        else:
            print("Insufficient funds for transfer")

acc1 = Bank_Account("Fiza Sohail", 12345, 5000)
acc2 = Bank_Account("Hifsa Tufail", 54321, 10000)

print(f"{acc1.owner_name}\nBalance: {acc1.balance}")

acc1.deposit(10000)
acc1.withdrawal(5000)
acc1.transfer(acc2, 2000)
acc2.check_balance()




