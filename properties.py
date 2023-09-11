class Customer:
    def __init__(self, name, new_bal):
        self.name = name
        if new_bal < 0:
           raise ValueError("Invalid balance!")
        self._balance = new_bal  

    # Add a decorated balance() method returning _balance        
    @property
    def balance(self): # this method return the _balance attribute value
        return self._balance

    # Add a setter balance() method
    @balance.setter # this decorator is used to define setter method for the balance property.
    # This method will be called when you try to assign a value to cust.balance=3000
    def balance(self, new_bal):
        # Validate the parameter value
        if new_bal < 0:
           raise ValueError("naqib ullah make error!")
        self._balance = new_bal
        print("Setter method called")
        
# Create a Customer        
cust = Customer("Belinda Lutz", 2000)
print(cust.balance) # this line  calls the @propery decorator method and return the _balance value.

# # Assign 3000 to the balance property
cust.balance = 3000  

# # # Print the balance property
print(cust.balance) # call the getter method again and retrieve the updated value of balance.

