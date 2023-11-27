class BankAccount():
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        self.balance -= amount
        if self.balance > 0:
            print("True")
        else:
            print("False")

account1 = BankAccount()
account2 = BankAccount()
account1.deposit(10000)
account2.deposit(5000)
print(account1.balance)
print(account2.balance)
account1.withdraw(2000)
account2.withdraw(3000)
print(account1.balance)
print(account2.balance)
account1.withdraw(3000)
account2.withdraw(4500)
print(account1.balance)
print(account2.balance)


# ewentualnie druga wersja wdg książki:

class BankAccount():
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        else:
             return False
        
account = BankAccount()
print(account.balance)
account.deposit(1000)
print(account.balance)
account.deposit(2000)
print(account.balance)
res = account.withdraw(1500)
print(res)
print(account.balance)
res = account.withdraw(3000)
print(res)
print(account.balance)




