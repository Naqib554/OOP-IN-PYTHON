class Employee:
    MIN_SALARY=30000 # created a class attribute
    def __init__(self,name,salary):
        self.name=name # created a instance attribute
        # use class name to access the class attribute
        if salary>=Employee.MIN_SALARY:
            self.salary=salary
        else:
            self.salary=Employee.MIN_SALARY    
emp1=Employee("TBD",40000)
print(emp1.MIN_SALARY) # same value accross multiple instances of the class attribute

emp2=Employee("TBD",60000)
print(emp2.MIN_SALARY) # same value accross multiple instances of the class attribute

