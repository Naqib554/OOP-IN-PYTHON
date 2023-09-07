# oop: code as interaction of objects
# great for building frameworks and tools
# making it more reusable and maintainable.

# object=state+behavior
# For example, an object representing a customer can have a certain phone number and email associated with them,
# and behaviors like placeOrder or cancelOrder.

# everything in python is object
# and every object has a class
# use type() method to find out the class


# State information in Python is contained in attributes,
#  and behavior information -- in methods.

# class and object:
#  Classes and objects both have attributes and methods, but the difference is that a class is an abstract template,
#   while an object is a concrete representation of a class.


 # what's self?
# In Python, "self" is a placeholder for future objects within a class definition.
#   It's used to access object-specific data and methods, and Python handles it automatically when calling methods from objects,
#    so we don't need to explicitly pass "self" as an argument.

# python will take care of self when method called from an object:
# will be interpreted as obj.Identify(obj,"naqibhangu1@gmail.com")
# That's why we don't specify it explicitly when calling the method from an existing object .


# In Python, when you use .name within a class method, it becomes an attribute when you assign a value to it using self.name = name

# Certainly! When you use self.count inside a class, it's like referring to a shared attribute that all objects of that class can access and modify.
# On the other hand, when you use mc.count, you're talking about a specific object's attribute. It's like each object having its own separate attribute.

# Well done! Notice how you used self.count to refer to the count attribute inside a class definition, and mc.count to refer to the count attribute of an object. Make sure you understand the difference,
#  and when to use which form (review the video if necessary)!



# A better strategy would be to add data to the object when creating it.

6. The right place to define attributes
# 02:20 - 03:08
# So, there are two ways to define attributes: 
# we can define an attribute in any method in a class; and then calling the method will add the attribute 
# to the object. Alternatively, we can define them all together in the constructor. If possible, 
# try to avoid defining attributes outside the constructor. Your class definition can be hundreds lines
#  of code long, and the person reading it would have to comb through all of them to find all the
#  attributes. Moreover, defining all attributes in the constructor ensures that 
#  all of them are created when the object is created, so you don't have to worry about trying to access
#  an attribute that doesn't yet exist. All this results 
# in more organized, readable, and maintainable code.

# note:
# defining attributes in the constructor easier to know all the attributes
