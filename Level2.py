import graphics as g
import Project as p
import Gate_Class as gate
import key_code as k
import Screen_Class as s




w=g.GraphWin("Maze 2", 1000, 750)

maze=g.Image(g.Point(500, 375), "Maze2.png")
maze.draw(w)

gate1=gate.Gate(w, "v",(350, 273), 90)
gate2=gate.Gate(w, 'h', (831, 167), 83)
gate3=gate.Gate(w, "h", (736, 323), 82)
gate4=gate.Gate(w, 'h', (545, 425), 82)
gate5=gate.Gate(w, "h", (448, 627), 82)
all_gates=[gate1, gate2, gate3, gate4, gate5]


key1=k.Key(w, 163, 365)
key2=k.Key(w, 255, 569)
key3=k.Key(w, 740, 475)
key4=k.Key(w, 350, 569)
all_keys=[key1, key2, key3, key4]
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