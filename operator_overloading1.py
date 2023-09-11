class Customer:
    def __init__(self,id,name):
        self.id,self.name=id,name
        print("The id:{} and name:{}".format(self.id,self.name))
    def __eq__(self,other):
        # "self.id " indicates the left side object from "==" and other.id refers to right side object from the "=="
        return (self.id==other.id) and (self.name==other.name) 
    
Customer1=Customer(22,"naqib")    
Customer2=Customer(22,"naqib")    
# __eq__() method is called implicitly when you use the == operator to compare objects of your class.
res=Customer1==Customer2 
print(res)
