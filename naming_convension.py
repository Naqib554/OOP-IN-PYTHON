class Employee:
    def __init__(self):
        self.public_variable="hangu" # public variable access by anyone
        # Single leading underscore for "protected" variable
        self._protected_variable = 123

        # Double leading underscores for name mangling (not inheritance prevention)
        self.__private_variable = "I am private" # this private variable not accessable outside the class
        print(self.__private_variable)

     # Public method
    def public_method(self):
        print("This is a public method")    

    # Single leading underscore for "protected" method
    def _protected_method(self):
        print("This is a protected method")

    

x=Employee()
print(x.public_variable)    
print(x._protected_variable)  
print(x._MyClass__private_variable)
x.public_method()
x._protected_method()



