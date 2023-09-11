class Customer:
    def __init__(self,name,balance):
        self.name,self.balance=name,balance

    def __str__(self):
        cust_str='''Customer:
        name:{name},
        balance:{balance}
        '''.format(name=self.name,balance=self.balance)
        return cust_str



obj=Customer('naqib',3000)
# a trigger refers to initiate an action or evern
print(obj) # when print the object this trigger  __str__() to be executed and return the string



# __str__() only accept the "self" argument and retrun the string to user
# similary the __repr__ also work the same like __str__() 
# the triple quotes are used in Python to define multi-line strings
