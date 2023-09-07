class Player:
    MAX_POSITION = 10
    
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

p = Player(); p.draw()
p.move(4); p.draw()
p.move(5); p.draw()
p.move(3); p.draw()
