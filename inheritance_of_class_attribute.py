class Player:
    class_attribute=" I am the class attribute in the parent class"

class Child(Player):
    pass

# Accessing the class attribute from both the Parent and Child classes
print("Parent class attribute",Player.class_attribute)
print("Child class attribute",Child.class_attribute)


# When we access the class_attribute from both the Parent and "Child classes",
# you'll see that the child class inherits the class attribute from its parent.
