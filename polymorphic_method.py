class Parent:
    def talk(self):
        print("Parent talking!")

class Child(Parent):
    def talk(self):
        print("Child talking!")

class TalkativeChild(Parent):
    def talk(self):
        print("TalkativeChild talking!")
        Parent.talk(self) # explacitlly call the talk() of parent class

p, c, tc = Parent(), Child(), TalkativeChild()

for obj in (p, c, tc):
    obj.talk()

# in the above code the talk() method of parent class is inherited
# by the subclasses of child and TalkativeChild