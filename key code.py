import graphics as g

class Key:
    keys_collected=0
    def __init__ (self, w, x, y):
        self.w=w
        self.x=x
        self.y=y
        self.make_key()
        self.make_counter()
        
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
        
    def print(self):
        return "Key at location {self.x}, {self.y}"
    
    def make_counter(self):
        """
        Makes the initial counter. Will always start with zero keys.
        """
        self.keys_text=g.Text(g.Point(30,25), "KEYS:")
        self.keys_number=g.Text(g.Point(60,25), str(Key.keys_collected))
        self.keys_text.setFill("white")
        self.keys_number.setFill("white")
        self.keys_text.draw(self.w)
        self.keys_number.draw(self.w)
        
    def collect_key(self):
        """
        Removes key from screen and adds key to counter.
        """
        self.loop.undraw()
        self.keybody.undraw()
        self.prong1.undraw()
        self.prong2.undraw()
        Key.keys_collected+=1
        self.keys_number.undraw()
        self.keys_number=g.Text(g.Point(60,25), str(Key.keys_collected))
        self.keys_number.setFill("white")
        self.keys_number.draw(self.w)
        player_keys.append(self)
    
    def use_key(self):
        """
        removes key from inventory and adjusts key counter
        """
        Key.keys_collected-=1
        self.keys_number.undraw()
        self.keys_number=g.Text(g.Point(60,25), str(Key.keys_collected))
        self.keys_number.setFill("white")
        self.keys_number.draw(self.w)
        player_keys.remove(self)
        
        
if __name__ == '__main__':
    w=g.GraphWin("test key", 1000, 750)
    w.setBackground("black")
    player_keys=[]
    key=Key(w,250,250)
    w.getMouse()
    key.collect_key()
    print(player_keys)
    w.getMouse()
    key.use_key()
    print(player_keys)
    w.getMouse()
    w.close()