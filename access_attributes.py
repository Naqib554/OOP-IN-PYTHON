class MyClass:
    def __init__(self):
        self.public_variable = 42  # Public variable
        self._protected_variable = 123  # Single leading underscore for "protected" variable
        self.__private_variable = "I am private"  # Double leading underscores for name mangling

    def __private1(self):
        print("I am private not available to anyone except the owner")    

# Creating an instance of the class
obj = MyClass()

# Accessing the private variable using the mangled name
print(obj._MyClass__private_variable)  # Output: I am private

# Accessing the private method using the mangled name
obj._MyClass__private1()  # Output: I am private not available to anyone except the owner




