class BankAccount:
    def __init__(self, account_no, balance=0):
        self.account_no = account_no
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance")

    def check_balance(self):
        print("Balance:", self.balance)

acc = BankAccount(1345, 1000)
acc.deposit(10000)
acc.withdraw(2000)
acc.check_balance()
