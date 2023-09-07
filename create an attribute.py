class CustomerData: # CamelCase
    def set_name(self,new_name): # lowercase for the function with underscore
        self.name=new_name

# Now the identify function will only use the data that is encapsulated in the object, instead of using whatever we passed to it.
    def Identify(self):
        print("I am a Customer "+self.name)    


# when object  created at this time .name doesn't exist here yet
cust=CustomerData()  
# after calling the set_name() method the attribute created and set to "naqibhangu1@gmail.com"
cust.set_name("naqibhangu1@gmail.com")
cust.Identify()
# how to access this attribute
# print(cust.name)


# remeber:
# Yes, the name attribute in this code is an attribute of the class instances (objects), not the class itself.