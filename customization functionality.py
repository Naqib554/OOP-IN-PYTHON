# Define the Employee class
class Employee:
    def __init__(self, name, salary=30000):
        # Initialize the Employee with a name and a default salary of 30000
        self.name = name
        self.salary = salary

    def give_raise(self, amount):
        # Give the employee a raise by adding the given amount to their salary
        self.salary += amount

# Define the Manager class, which is a subclass of Employee
class Manager(Employee):
    def display(self):
        # Display the manager's name
        print("Manager ", self.name)

    def __init__(self, name, salary=50000, project=None):
        # Initialize the Manager with a name, a default salary of 50000, and an optional project
        Employee.__init__(self, name, salary) # call the parent class constructor
        self.project = project

    # Override the give_raise method from the Employee class
    def give_raise(self, amount, bonus=1.05):
        # Calculate the new amount by applying a bonus factor
        new_amount = amount * bonus
        # Call the give_raise method from the Employee class to actually give the raise
        Employee.give_raise(self, new_amount)

# Create a Manager instance named mngr with a name "Ashta Dunbar" and an initial salary of 78500
mngr = Manager("Ashta Dunbar", 78500)

# Give the manager a raise of 1000
mngr.give_raise(1000)
# Print the manager's updated salary
print(mngr.salary)

# Give the manager a raise of 2000 with a custom bonus of 1.03
mngr.give_raise(1000, bonus=1.03)
# # Print the manager's updated salary
print(mngr.salary)


# execution process of the above code:
# when only the object is created:
# the manager class inherits from the employee class so first the employee class __init__() interpreted
# it create name and salary attributes for the manager class object. 
# then the manager class has own constructor called and set to additional attributes specific to managers.
# in the above case is project .
# and so on 


