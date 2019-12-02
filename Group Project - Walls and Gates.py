import graphics as g

class Wall:
    def __init__(self, w, point1):
        self.w = w
        self.point1x = point1[0]
        self.point1y = point1[1]
        self.point2x = self.point1x + 10
        self.point2y = self.point1y + 10
        self.build()
        
    def print(self):
        return f"tile: wall segment at coordinates {self.point1}"
    
    def build(self):
        brick = g.Rectangle(g.Point(self.point1x, self.point1y), g.Point(self.point2x, self.point2y))
        brick.setFill('white')
        brick.draw(self.w)


class Gate:
    def __init__(self, w, point1):
        self.w = w
        self.point1x = point1[0]
        self.point1y = point1[1]
        self.point2x = self.point1x + 10
        self.point2y = self.point1y + 50
        self.build()
    
    def print(self):
        return f"tile: gate at coordinates {self.point1}"
    
    def build(self):
        door = g.Rectangle(g.Point(self.point1x, self.point1y), g.Point(self.point2x, self.point2y))
        door.setFill('yellow')
        door.draw(self.w)

w = g.GraphWin("test", 1000, 750)
w.setBackground('black')
maze = {}

for key in maze:
    if maze[key] == 1:
        wall = Wall(w, key)
    elif maze [key] == 2:
        gate = Gate(w, key)