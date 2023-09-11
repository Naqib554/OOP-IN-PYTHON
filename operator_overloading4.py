# Comparison and inheritance:
# What happens when an object is compared to an object of a child class? Consider the following two classes:

class Parent:
    def __eq__(self, other):
        print("Parent's __eq__() called")
        return True

class Child(Parent):
    def __eq__(self, other):
        print("Child's __eq__() called")
        return True
import numpy as np
# this return a an object 
arr=np.array([1,2,3])    

# this is custom class object 
p = Parent()
c = Child()

p == c 

print(arr) # normal object with print(): this return the actual data that it contains
print(p) # custom class object with print(): this return the memory address

# Python always calls the _child's_ __eq__() method when comparing a child object to a parent object.