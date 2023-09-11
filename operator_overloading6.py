class Customer:
    def __init__(self,name,balance):
        self.name,self.balance=name,balance


    def __repr__(self):
        return "Customer:('{name}','{balance})'".format(name=self.name,balance=self.balance)

obj=Customer("naqib",345)
print(obj) # this trigger the __repr__()  to be executed

# There are two special methods in Python that return a string representation of an object
# the main purpouse of these two methods is used to see the custom object data
# 1)__str__()
# 2)__repr__()

