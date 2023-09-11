class Account:
    def __init__(self, number, balance=0):
        self.number, self.balance = number, balance
      
    def withdraw(self, amount):
        self.balance -= amount 

    def __eq__(self, other):
        # type check whether the objects belong to same class or not
        return (self.number == other.number) and (type(self) == type(other))

class BankAccount(Account):
    pass

# Create a BankAccount object
acct = Account(873555333)

# # Create a BankAccount object with the same account number
acct2 = Account(873555333)

# # Create a BankAccount object with a different account number
acct3 = Account(2345642)

# # Compare BankAccount objects
print(acct == acct2)  # This will return True because they have the same account number.
print(acct == acct3)  # This will return False because they have different account numbers.
