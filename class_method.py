class Employee:
    
    def __init__(self, name, salary=0):
        # create name and salary attributes in the constructor
        self.name = name
        # Modify code below to check if salary is positive
        if salary >= 0:
            self.salary = salary
        else:
            self.salary = 0
            print("Invalid salary!")
    
    @classmethod
    def from_file(cls, filename):
        with open(filename, "r") as f:
            name = f.read()
        return cls(name)

# Now, let's call the class method to create an Employee object from a file:
# You define a class method called from_file. This class method is designed to create Employee objects based on data from a file.
employee_from_file = Employee.from_file("hangu.txt")

# You can access the attributes of the newly created employee object:
print("Name:", employee_from_file.name)
print("Salary:", employee_from_file.salary)






