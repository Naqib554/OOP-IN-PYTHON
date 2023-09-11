class BankAccount:
     # MODIFY to initialize a number attribute
    def __init__(self, number, balance=0):
        self.balance = balance
        self.number = number
      
    def withdraw(self, amount):
        # withdraw the given amount from the actual balance
        self.balance -= amount 
        print(self.balance)

    # Define __eq__ that returns True if the number attributes are equal 
    def __eq__(self, other):
        return (self.number == other.number)   
    
acct1 = BankAccount(123, 1000)
# acct1.withdraw(100)
acct2 = BankAccount(123, 1000)
# acct1.withdraw(200)
acct3 = BankAccount(456, 1000)
# acct1.withdraw(300)

print(acct1 == acct2) # while comparing objects the __eq__() called atutomatically
print(acct1 == acct3)
    