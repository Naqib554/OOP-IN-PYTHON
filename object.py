class Person:
    def __init__(self, name, age):
        self.name = name  # Attribute to store the name
        self.age = age    # Attribute to store the age

    def say_hello(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Creating objects (instances) of the Person class
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

# Each object has its own data stored in its attributes
print(person1.name)  # Output: "Alice"
print(person2.name)  # Output: "Bob"

# Calling a method on an object
person1.say_hello()  # Output: "Hello, my name is Alice and I am 30 years old."
person2.say_hello()  # Output: "Hello, my name is Bob and I am 25 years old."
