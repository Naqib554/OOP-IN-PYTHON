class Player:
    class_attribute=" I am the class attribute in the parent class"

class Child(Player):
    class_attribute=45  #  This overrides the class_attribute of the parent class for instances of the Child class.
    pass

# Accessing the class attribute from both the Parent and Child classes
print("Parent class attribute",Player.class_attribute)
print("Child class attribute",Child.class_attribute)
