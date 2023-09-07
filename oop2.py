# Define a class representing an employee
class Employee:
    def __init__(self, name, salary):
        # name and salary varibles are object(mystery) attributes not the class attributes
        self.name = name
        self.salary = salary
    # the class method use 'self' to work with object attributes 
    def give_raise(self, amount):
        # Access the salary attribute of the object(mystery) using self.salary
        self.salary += amount

# Create an instance of the Employee class for the mystery employee
mystery = Employee("John Doe", 50000)

# Print the mystery employee's name
print("Mystery employee's name:", mystery.name)

# Print the mystery employee's salary
print("Mystery employee's salary:", mystery.salary)

# the give_raise method accesses and modifies the salary attribute of the employee class object(mystery)
mystery.give_raise(2500)

# Print the salary again
print("Mystery employee's new salary after the raise:", mystery.salary)
