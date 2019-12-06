
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
        
        x1 = self.player.getP1().getX() 
        y1 = self.player.getP1().getY()
        #upper left coordinates (x1,y2)
        x2 = self.player.getP2().getX()
        y2 = self.player.getP2().getY()
        #lower right coordinates (x2,y2)
        #upper right coordinates (x2,y1)
        #lower left coordinates (x1,y2)
        
        all_coordinates = [[x1,y1],[x2,y2],[x2,y1],[x1,y2]]
        
        for coordinate in all_coordinates:
            x = int(coordinate[0])
            y = int(coordinate[1])
            colors = image.getPixel(x,y)
            
            #will return a list of numbers for each coordinate color
            if colors[0] > 245 and colors[1] > 245 and colors[2] > 245:
            #greater than 245 for each element = white
                return True

        return False 
            #this will work in a for loop
            #because if at any point the if statement isn't true, it'll break out
            #put return False outside of if statement so it will check all coordinates
    
    def end_spot(self):
        
        #end_spot = g.Rectangle(g.Point(600,325),g.Point(700,425))
        #end_spot_center = g.Point(950,375)
        
        end_point = g.Circle(g.Point(950,375),20)
        end_point.setFill("grey")
        end_point.draw(w)
        
        x1 = self.player.getP1().getX() 
        y1 = self.player.getP1().getY()
        x2 = self.player.getP2().getX()
        y2 = self.player.getP2().getY()
        
        #p1 = [x1,y1]
        #p2 = [x2,y2]
        #p1 = upper left coordinate
        #p2 = lower right coordinate
        
        if (x1 < 950 < x2) and (y1 < 375 < y2):
            return True
        else:
            return False
        
    def undraw(self):
        self.player.undraw(w)
        
if __name__== "__main__":

    w = g.GraphWin("Game",1000,750)
    w.setBackground("black")
    
    #start spot at 100 by 375
    #end spot at 650 by 375 
           
    maze = g.Image(g.Point(500,375),"Maze2.png")
    maze.draw(w)
    #how to actually draw it in the window? 
      
    Player1 = Player(w,50,375)
    
    key = None
    
    while Player1.end_spot() == False:
        key = w.checkKey()
        Player1.control()
        if Player1.collision_detection(maze) == True:
            Player1.player.undraw()
            Player1 = Player(w,50,375)
    w.getMouse()    
    w.close()   

#check corners to see if they're black (wall color) (0,0,0)
#getPixel(x,y)
#setPixel(x,y,Color)
'''
create gif same size as window with black walls 
plop the image into the window (theoretically the same size so coordinates match)
if any of my four corners hits something black - signify end of game

'''
    
    
    
    
