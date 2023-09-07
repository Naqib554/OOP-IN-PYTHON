class Employee:
  
  def set_name(self, new_name):
    # using attribute in a class definition
    self.name = new_name
  
  # Add set_salary() method  
  def set_salary(self, new_salary):
    # using attribute in a class definition
    self.salary = new_salary 
  
  
# Create an object emp of class Employee  
emp = Employee()

# Use set_name to set the name of emp to 'Korel Rossi'
emp.set_name('Korel Rossi')
print(emp.name)

# Set the salary of emp to 50000
emp.set_salary(50000)
print(emp.salary)

# Increase salary of emp by 1500
emp.salary = emp.salary + 1500
print(emp.salary)


