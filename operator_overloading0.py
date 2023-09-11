class Customer:
    def __init__(self,name,balance,id):
        self.name,self.balance=name,balance
        self.id=id

Customer1=Customer("Naqib",2000,33)
Customer2=Customer("Naqib",2000,33)
print(Customer1)
# when an object is created, Python allocates a chunk of memory to that object
# here we compare two chunk of memory therby it return "False", not compare the data that object contains
if Customer1==Customer2:
    print("True")
else:
    print("False")

    