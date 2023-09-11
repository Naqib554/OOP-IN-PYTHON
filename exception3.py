class SalaryError(ValueError):
    pass

class BonusError(SalaryError):
    pass

class Employee:
    MIN_SALARY = 30000
    MAX_BONUS = 5000

    def __init__(self, name, salary=30000):
        self.name = name
        if salary < Employee.MIN_SALARY:
            raise SalaryError("Salary is too low!")
        self.salary = salary

    # Rewrite using exceptions
    def give_bonus(self, amount):
        if amount > Employee.MAX_BONUS:
            raise BonusError("The bonus amount is too high!") # this specific message will replaced by "{e}" in the bellow

        if self.salary + amount < Employee.MIN_SALARY:
            raise SalaryError("The salary after bonus is too low!")

        self.salary += amount

# Example usage:
try:
    emp = Employee("John", 35000)
    emp.give_bonus(4000)

#The except SalaryError as e: block catches the SalaryError exception
# and assigns it to the variable e, which becomes an instance of the SalaryError class.
except SalaryError as e: 
    # the {e} will replaced by the above actual message if this type error occure in the code.
    print(f"SalaryError: {e}")
 # Yes, in the line except BonusError as e:, the variable e becomes an object of the BonusError class
except BonusError as e: # the except keyword handle the error
    print(f"BonusError: {e}")
else:
    print(f"{emp.name}'s new salary: ${emp.salary}")
