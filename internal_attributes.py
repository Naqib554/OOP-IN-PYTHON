# Add class attributes for max number of days and months
class BetterDate:
    _MAX_DAYS = 30
    _MAX_MONTHS = 12
    
    def __init__(self, year, month, day):
        self.year, self.month, self.day = year, month, day
        

    @classmethod
    def from_str(cls, datestr):
        date_string=datestr.split("-") #--> convert string into the list 
        print(date_string)
        year,month,day=map(int,date_string)
        # print(year)
        # or the three reduce to the one line code like bellow
        # year, month, day = map(int, datestr.split("-"))
        return cls(year,month,day)

    
    # Add _is_valid() checking day and month values
    def _is_valid(self):
        return (self.day <= BetterDate._MAX_DAYS) and \
               (self.month <= BetterDate._MAX_MONTHS)
        

date_str = "2021-09-10"

obj=BetterDate.from_str(date_str) # this is the way to call the class method in python

z=obj._is_valid() # call the class object method 
print(z)

