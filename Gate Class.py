import graphics as g

class Gate:
    def __init__(self, w, ori, point, length):
        self.w = w
        self.ori = ori #orientation. determines whether the gate is vertical (v) or horizontal (h).
        self.pointx = point[0] #determines the gate's CENTERPOINT
        self.pointy = point[1]
        self.length = length #how long the gate is. set this to fill the maze gap
        self.build()
        
    def print(self):
        if self.ori == 'v':
            return f"vertical gate located at {self.pointx}, {self.pointy}"
        elif self.ori == 'h':
            return f"horizontal gate located at {self.pointx}, {self.pointy}"
        
    def build(self):
        if self.ori == 'v': #if the gate is meant to be vertical
            self.point1x = self.pointx - 5 #determines that the gate is 10 pixels thick
            self.point1y = self.pointy - (self.length // 2) #determines that the gate is the specified length
            self.point2x = self.pointx + 5
            self.point2y = self.pointy + (self.length // 2)
        elif self.ori == 'h': #if the gate is meant to be horizontal
            self.point1x = self.pointx - (self.length // 2)
            self.point1y = self.pointy - 5
            self.point2x = self.pointx + (self.length // 2)
            self.point2y = self.pointy + 5
        door = g.Rectangle(g.Point(self.point1x, self.point1y), g.Point(self.point2x, self.point2y))
        door.setFill('yellow') # red:255, green:255, blue:0
        door.draw(self.w)
        
win = g.GraphWin("test", 200, 200)
win.setBackground('black')
doorv = Gate(win, 'v', (50, 50), 80)
doorh = Gate(win, 'h', (100, 100), 45)