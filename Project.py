
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
            
    def get_player_xposition(self):
        x = Player.getCenter().getX()
        return x
        
    def get_player_yposition(self):
        y = Player.getCenter().getY()
        return y


if __name__== "__main__":

    w = g.GraphWin("Game",750,1000)
    w.setBackground("black")
    
    start_spot = g.Rectangle(g.Point(75,350),g.Point(125,400))
    #start spot center at 100 by 375
    start_spot.setFill("grey")
    start_spot.draw(w)
    #spawn point
    
    end_spot = g.Rectangle(g.Point(600,325),g.Point(700,425))
    #end spot center at 650 by 375
    #end spot slightly bigger than player
    end_spot.setFill("black")
    end_spot.draw(w)
    
    Player = Player(w,100,375)
    x = Player.get_player_xposition
    y = Player.get_player_yposition
    #should these be stored or what? how will this interact with hayden's maze
    #absolutely noooooooooooo idea 
        
    key = None
    while key != "q":
        key = w.checkKey()
        Player.control()
    w.close()   
    
    
    
    
    #while 480 > x and x > 520 and y < 355 and y > 395:
       #key = w.checkKey()
    #Player.control()
    #w.getMouse()
    #w.close()
    
    #need to change while condition 
    #when the player is inside the endpoint - get mouse and then end (or something)     
    
