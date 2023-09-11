class Employee:
    def display(self):
       self.name="naqib"
       print("this is my name:",self.name)
class child(Employee):
    def display(self):
        print("my eduction is 16 and still I am studying rightnow.")
        Employee.display(self)
        Employee.display(self)
child1=child()    
child1.display()
