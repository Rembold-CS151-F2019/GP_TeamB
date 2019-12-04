
import graphics as g

class Player:
    
    def __init__ (self,w,x,y):
        self.w = w
        self.x = x
        self.y = y
        self.create()
        
    def create(self):
        self.player = g.Rectangle(g.Point(self.x-25,self.y-25),g.Point(self.x+25,self.y+25))
        #should be a 50x50 rectangle
        self.player.setFill("red")
        self.player.draw(w)
        
    def control(self):
        if key == "Up" or key == "w":
            self.player.move(0,-5)
        elif key == "Down" or key == "s":
            self.player.move(0,5)
        elif key == "Left" or key == "a":
            self.player.move(-5,0)
        elif key == "Right" or key == "d":
            self.player.move(5,0)
            
    def collision_detection(self,image):
        
        x1 = self.player.getP1.getX() 
        y1 = self.player.getP1.getY()
        #upper left coordinates (x1,y2)
        x2 = self.player.getP2.getX()
        y2 = self.player.getP2.getY()
        #lower right coordinates (x2,y2)
        #upper right coordinates (x2,y1)
        #lower left coordinates (x1,y2)
        
        all_coordinates = [[x1,y1],[x2,y2],[x2,y1],[x1,y2]]
        
        for coordinate in all_coordinates:
            x = coordinate[0]
            y = coordinate[1]
            colors = image.getPixel(x,y)
            #will return a list of numbers for each coordinate color
            if colors[0] < 10 and colors[1] < 10 and colors[2] < 10:
            #less than ten for all elements = color black
                return True
            else:
                return False 
            #this will work in a for loop
            #because if at any point the if statement isn't true, it'll break out


        #what do I want it to do if it does detect a collision?
            #probably stop and wait for a mouseclick or something
        #i need an example gif 
        
    def end_spot(self):
        
        #end_spot = g.Rectangle(g.Point(600,325),g.Point(700,425))
        
        x1 = self.player.getP1.getX() 
        y1 = self.player.getP1.getY()
        x2 = self.player.getP2.getX()
        y2 = self.player.getP2.getY()
        
        p1 = [x1,y1]
        p2 = [x2,y2]
        #p1 = upper left coordinate
        #p2 = lower right coordinate
        
        if 600 < p1[0] < 700 and 325 < p1[1] < 425 and 600 < p2[0] < 700 and 325 < p2[1] < 425:
            return True
        else:
            return False 
       
if __name__== "__main__":

    w = g.GraphWin("Game",750,1000)
    w.setBackground("black")
    
    Player = Player(w,100,375)
    
    
    #start spot at 100 by 375
    #end spot at 650 by 375 
           
    #maze = g.Image(g.Point(375,500),"Maze.gif")
    #how to actually draw it in the window? 
       
    key = None
    while key != "q":
        key = w.checkKey()
        Player.control()
        #Player.collision_detection(Maze)
    w.close()   

#check corners to see if they're black (wall color) (0,0,0)
#getPixel(x,y)
#setPixel(x,y,Color)
'''
create gif same size as window with black walls 
plop the image into the window (theoretically the same size so coordinates match)
if any of my four corners hits something black - signify end of game

'''
    
    
    
    
