class Customer:
   
    def Identify(self,name):
        print("I am the Customer "+name)

    #   set the name attribute of an object to a new_name
    def set_name(self,new_name):
        # create an attribute by assigning  a value
        self.name=new_name 

obj=Customer()

# keep in mind that the method call doesn't require "self".ignore self when calling method on an object
obj.Identify("naqibhangu1@gmail.com")
# when the set_name method called the above self.name attribute was created and 
# set self.name="hangu"
obj.set_name("hangu")
# we access it by using its name
print(obj.name)