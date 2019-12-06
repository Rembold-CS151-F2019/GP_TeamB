import graphics as g
import Project as p
import Gate_Class as gate
import key_code as k
import Screen_Class as s





w=g.GraphWin("Maze 1", 1000, 750)
maze=g.Image(g.Point(500, 375), "Maze1improved.png")
maze.draw(w)

gate1=gate.Gate(w, "v",(250,362), 160)
gate2=gate.Gate(w, "v", (580,362), 160)
gate3=gate.Gate(w, "v", (790,362),160)
all_gates=[gate1, gate2, gate3]


key1=k.Key(w, 130,115)
key2=k.Key(w, 430, 630)
key3=k.Key(w, 855, 100)

all_keys=[key1, key2, key3]
player=p.Player(w, 60, 360)

end_point = g.Circle(g.Point(950,375),20)
end_point.setOutline("green")
end_point.draw(w)

k.make_counter(w)
player_key_list=[]

keyboard=None
while keyboard!= "q":
    keyboard=w.checkKey()
    player.control(keyboard)
    if player.collision_detection(maze) == False:
        
        for key in all_keys.copy():
            if player.overlap_key(key)==True:
                player_key_list.append(key)
                k.collect_key(key)
                all_keys.remove(key)
                key=None
                
           
        for gates in all_gates:
            
            if player.overlap_gate(gates)==True:
                if k.Key.keys_collected>0:
                    gates.delete()
                    all_gates.remove(gates)
                    gates=None
                    k.use_key(player_key_list[0])

                else:
                    you_died=s.Death(w)
                    player.undraw()
                    w.after(1000)
                    you_died.undraw()
                    player=p.Player(w, 60, 360)
        
    if player.end_spot()==True:
        you_won=s.Win(w)
        player.undraw()
        keyboard=w.getKey()
        
        
    if player.collision_detection(maze) == True:
        you_died=s.Death(w)
        player.undraw()
        w.after(1000)
        you_died.undraw()
        player=p.Player(w, 60, 360)
        
       
        
w.close()