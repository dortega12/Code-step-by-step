class BankAccount:
    def __init__(self, name, balance = 0.0):
        self.name = name
        self.balance = balance

    def deposit(self, depo):
        self.balance += depo
        return self.balance

    def withdraw(self, wdraw):
        self.balance -= wdraw
        return self.balance
        
def main():
    name = input("What is the name under your acount? ")
    initial = float(input("How much money is in your bank account?"))
    
    depo = float(input("how much money would you like to deposit? "))
    wdraw = float(input("how much would you like to withdraw? "))
    ba = BankAccount(name, initial)
    
    print(name)
    print(ba.deposit(depo))
    print(ba.withdraw(wdraw))
    
main()
