1)class attribute:
# the class attribute serve as a global varibles within the class.
# the class attribute will be shared among all the instances of the employee/any class
# and the value of the class attribute will be the same across instances
# use the class name to access the class attribute

2) Why use class attributes?
# So, the main use case for class attributes is global constants that are related to class, 
# for example min/max values for attributes -- like the min_salary example -- or commonly used values: 
# for example,if you were defining a Circle class, you could store pi as a class attribute.

3) About Method:
# Regular methods are already shared between instances: the same code gets executed for every instance. 
# The only difference is the data that is fed into it
# -->  To define a class method, you start with a classmethod decorator, followed by a method definition.
# The only difference is that now the first argument is not self, but cls, referring to the class,
# just like the self argument was a reference to a particular instanc
note:
# these class methods cannot access instance-level data, 
# and they are called using the class name, not an instance
# class methods can't use instance level data

why we need class method:
# So, class methods are like special instructions to create objects 
# in unique ways when the usual method won't work.

class level and instance level attributes:
# The class attribute is shared by all instances of the class, 
# while the instance attribute is unique to each object.





