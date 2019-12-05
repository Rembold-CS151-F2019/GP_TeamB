import graphics as g


class Key:
    keys_collected=0
    def __init__ (self, w, x, y):
        self.w=w
        self.x=x
        self.y=y
        self.make_key()
        
    def make_key(self):
        """
        this just makes the key graphic/icon. Can be adjusted as needed.
        """
        self.loop= g.Rectangle(g.Point(self.x-5,self.y),g.Point(self.x+5,self.y-10))
        self.loop.setWidth(2)
        self.loop.setOutline("yellow")
        self.keybody=g.Line(g.Point(self.x, self.y), g.Point(self.x, self.y+15))
        self.keybody.setWidth(2)
        self.keybody.setOutline("yellow")
        self.prong1=g.Line(g.Point(self.x, self.y+8),g.Point(self.x+5, self.y+8))
        self.prong2=g.Line(g.Point(self.x, self.y+14),g.Point(self.x+5, self.y+14))
        self.prong1.setWidth(2)
        self.prong1.setOutline("yellow")
        self.prong2.setWidth(2) 
        self.prong2.setOutline("yellow")
        self.loop.draw(self.w)
        self.keybody.draw(self.w)
        self.prong1.draw(self.w)
        self.prong2.draw(self.w)
        
    
def make_counter(window):
    """
    Makes the initial counter. Will always start with zero keys.
    """
    global keys_text

    keys_text=g.Text(g.Point(30,25), f"KEYS:{str(Key.keys_collected)}")
        
    #self.keys_number=g.Text(g.Point(60,25), ))
        
    keys_text.setFill("grey")
    #self.keys_number.setFill("grey")
    keys_text.draw(window)
    #self.keys_number.draw(self.w)
    
        
def collect_key(key):
    """
    Removes key from screen and adds key to counter. requires key object type input
    """
    global keys_text
    
    if key!=None:
        key.loop.undraw()
        key.keybody.undraw()
        key.prong1.undraw()
        key.prong2.undraw()
        
        Key.keys_collected+=1
        keys_text.undraw()
        
        keys_text=g.Text(g.Point(30,25), f"KEYS:{str(Key.keys_collected)}")
        keys_text.setFill("grey") 
        keys_text.draw(key.w)
    
def use_key(key):
    """
    removes key from inventory and adjusts key counter
    """
    global keys_text
    
    Key.keys_collected-=1
    keys_text.undraw()
    keys_text=g.Text(g.Point(30,25), f"KEYS:{str(Key.keys_collected)}")
    keys_text.setFill("grey")
    keys_text.draw(key.w)
        
        
if __name__ == '__main__':
    w=g.GraphWin("test key", 1000, 750)
    w.setBackground("black")
    player_keys=[] #a player_keys list will be needed in the final compiling
    key=Key(w,250,250)
    key.make_counter
    w.getMouse()
    key.collect_key()
    w.getMouse()
    key.use_key()
    w.getMouse()
    w.close()