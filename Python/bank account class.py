class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        
    def deposit(self, depo):
        result = self.balance + depo
        if result > 0:
            self.balance = result
        return self.balance
        
    def withdraw(self, withdraw):
        result = self.balance - withdraw
        if result >= 0:
            self.balance = result       
        return self.balance
        
def main():
    name = input("What is the name under your acount? ")
    initial_balance = float(input("initial balance? "))
    
    depo = float(input("how much money would you like to deposit? "))
    withdraw = float(input("how much would you like to withdraw? "))
    ba = BankAccount(name, initial_balance)
    
    print(name)
    print(ba.deposit(depo))
    print(ba.withdraw(withdraw))
    
main()