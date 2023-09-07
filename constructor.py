class CustomerData: # CamelCase
    def __init__(self,name,balance=0): # <-- balance perameter added
        #  when the Customer class object is createdj, it will have the name attribute with the value provided
        self.name=name
        self.balance=balance # <-- balance attribute added
        print("The __init__ method was called")

cust=CustomerData("Naqib Ullah") # don't  specify  balance explacitly 
print(cust.name) #  Access the name attribute
print(cust.balance) # access the balance attribute



