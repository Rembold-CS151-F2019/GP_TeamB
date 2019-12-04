import graphics as g

class Screen:
    def __init__(self, w):
        self.w = w
    
    def bar(self):
        self.aha = g.Rectangle(g.Point(0, 350), g.Point(1000, 400))
        self.aha.setFill('black')
        self.aha.draw(self.w)
        

class Death(Screen):
    def __init__(self, w):
        self.w = w
        Screen.__init__(self.w)
        self.bar()
        self.death()
    
    def death(self):
        self.message = g.Text(g.Point(500, 375), "YOU DIED")
        self.message.setTextColor('red')
        self.message.draw(self.w)


class Win(Screen):
    def __init__(self, w):
        self.w = w
        Screen.__init__(self.w)
        self.bar()
        self.win()
    
    def win(self):
        self.message = g.Text(g.Point(500, 375), "A WINNER IS YOU")
        self.message.setTextColor('yellow')
        self.message.draw(self.w)

win = g.GraphWin('test', 1000, 750)
screen = Death(win)
win.getMouse()
win.close()