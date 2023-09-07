class Player:
    MAX_POSITION = 10
    MAX_SPEED=20
    
    def __init__(self):
        self.position = 0

    # Add a move() method with steps parameter     
    def move(self, steps):
        if self.position + steps < Player.MAX_POSITION:
           self.position = self.position + steps 
           print("The position value is :",self.position)
        else:
           self.position = Player.MAX_POSITION
           print("The position values increased to MAX_POSITION")
    
    # This method provides a rudimentary visualization in the console    
    def draw(self):
        
        # here the "-" is multiply by (self.position) value
        drawing = "-" * self.position + "|" +"-"*(Player.MAX_POSITION - self.position)
        print(drawing)

# create two objects p1 and p2
P1,P2=Player(),Player()

print("MAX_SPEED of p1 and p2 before assignment:")
print(P1.MAX_POSITION)
print(P2.MAX_SPEED)        

# Assign 7 to p1.MAX_SPEED 
P1.MAX_SPEED=7

print("MAX_SPEED of p1 and p2 after assignment:")
# Print p1.MAX_SPEED and p2.MAX_SPEED
print(P1.MAX_SPEED)
print(P2.MAX_SPEED)

print("MAX_SPEED of Player:")
# Print Player.MAX_SPEED
print(Player.MAX_SPEED)


