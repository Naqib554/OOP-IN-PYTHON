class Mycount:
    def Set_Count(self,n):
        self.count=n
        print("The value of count is :",self.count)
mc=Mycount()
mc.Set_Count(5)

# increase the value of count attribute
# mc.count is used to access the attribute of a particular object (mc in this example).
mc.count=mc.count+1
print("The value of count is :",mc.count)