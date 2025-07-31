from os import system
if system("clear") != 0: system("cls")

class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance
        self.is_active = True

    def deposit(self, amount):
        if not self.is_active:
            print("Account is inactive. Cannot deposit.")
        elif amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if not self.is_active:
            print("Account is inactive. Cannot withdraw.")
        elif amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Withdrawal amount must be positive and less than or equal to the current balance.")

    def get_balance(self):
        return self.balance


alice_account = BankAccount("Alice", 1000)
bob_account = BankAccount("Bob", 500)
gustavo_account = BankAccount("Gustavo", 2000000)

print(f"{gustavo_account.account_holder} has a balance of ${gustavo_account.get_balance():.2f}")
gustavo_account.deposit(5500)
print(f"{gustavo_account.account_holder} has a balance of ${gustavo_account.get_balance():.2f}")