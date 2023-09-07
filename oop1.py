# use type() to find the class
import numpy as np
ar=np.array([1,2,3,4])
print(type(ar))

# every numpy array has an attribute shape
print(ar.shape)

# it has also methods like bellow
print(ar.reshape(2,2))
# object = attributes(variables) + methods(functions)




class Person:     
    class_varible = "I'm a class variable"  # This is a class variable 
    print(class_varible)
    def __init__(self, name, age):
        self.name = name  # attribute 1 : this is an instance varible
        self.age = age    # attribute 2 : this is an instance varible

# Creating an instance of the Person class
person = Person("Alice", 30)

# The object 'person' has a state with 'name' and 'age' attributes:
print(person.name)  # Output: "Alice"
print(person.age)   # Output: 30
