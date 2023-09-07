class Employee:
  MIN_SALARY = 30000    

  def __init__(self, name, salary=MIN_SALARY):
      self.name = name
      if salary >= Employee.MIN_SALARY:
        self.salary = salary
      else:
        self.salary = Employee.MIN_SALARY
        
  def give_raise(self, amount):
      self.salary += amount # add the amonut in the salary attribute
        
# MODIFY Manager class and add a display method 
class Manager(Employee):
  def display(self):
     print("Manager",self.name)
     print("salary of manager is :",self.salary)

# Define a Manager object
mng = Manager("Debbie Lashko", 6000)
mng.give_raise(1000) # call give_raise method by the child class object
# Print mng's name
print(mng.name)
print(mng.salary)
mng.display()


# Excellent! You already started customizing! The Manager class now includes functionality that wasn't present in the original class (the display() function) in addition to all the functionality of the Employee class. 
# Notice that there wasn't anything special about adding this new method.

