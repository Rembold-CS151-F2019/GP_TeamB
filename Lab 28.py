import graphics as g
import random 

class Rectangle:
    
    def __init__(self, window, p1, p2, color):
        self.w = window
        self.p1 = p1
        self.p2 = p2 
        self.color = color
        self.draw()
        
    def draw(self):
        self.shape = g.Rectangle(self.p1, self.p2)
        self.shape.setFill("red")
        self.shape.draw(self.w)
        
    def In_range(self, point):
    #checks if the mouseclick point is within the rectangle itself 
        if self.p1.getX() < point.getX() < self.p2.getX():
        #checking x range
            if self.p1.getY() < point.getY() < self.p2.getY():
            #checking y range
                return True
        return False
        #needed otherwise it will return nothing
       
        
    def Move_random(self):
    #function to move square if mouse click is inside range 
        new_point = g.Point(random.randint(0,500),random.randint(0,500))
        #changed the range to 500 by 500 so entire rectangle will show up
        dx = -self.p1.getX() + new_point.getX()
        dy = -self.p1.getY() + new_point.getY()
        self.shape.move(dx,dy)
        self.p1 = self.shape.getP1()
        self.p2 = self.shape.getP2()
        #need to update points of new rectangle here for future clicking 
    
    
w = g.GraphWin('Window', 600, 600)
w.setBackground("white")
S1 = Rectangle(w,g.Point(100,100),g.Point(200,200),"red")
#w.getMouse()


key = ""

while key != "q":
    pt = w.checkMouse()
    if pt:
    #if pt is something (not None)
        if S1.In_range(pt):
            S1.Move_random()
    key = w.checkKey()
w.close()

#"check" will look for presence of key or mouse click
#if found, will take it, otherwise will return None 


                
    

