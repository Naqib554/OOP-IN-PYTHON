# Main Use Of Class Method: 
# The main use of class methods is defining methods that return an instance of the class,
#   but aren't using the same code as __init__()

class BetterDate:
    # Constructor
    def __init__(self, year, month, day):
      # Recall that Python allows multiple variable assignments in one line
      self.year, self.month, self.day = year, month, day
    
    # Define a class method from_str
    @classmethod
    def from_str(cls, datestr):
         # Split the string at "-" and  convert each part to integer
        parts = datestr.split("-")  # split the string into the list by the split method
        print(type(parts))

        year, month, day = int(parts[0]), int(parts[1]), int(parts[2])
        # Return the class instance
        return cls(year, month, day)
        

bd = BetterDate.from_str('2020-04-30')   
print(bd.year)
print(bd.month)
print(bd.day)
