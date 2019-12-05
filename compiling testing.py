import graphics as g
import Project as p
import Gate_Class as gate
import key_code as k
import Screen_Class as s










w=g.GraphWin("test maze", 1000, 750)
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

key1.make_counter()
player_key_list=[]

keyboard=None
while keyboard!= "q":
    keyboard=w.checkKey()
    player.control(keyboard)
    if player.collision_detection(maze) == False:
        
        for key in all_keys:
            if player.overlap_key(key)==True:
                player_key_list.append(key)
                key.collect_key()
                all_keys.remove(key)
                key=None
                
           
        for gate in all_gates:
            
            if player.overlap_gate(gate)==True:
                if k.Key.keys_collected>0:
                    gate.delete()
                    all_gates.remove(gate)
                    gate=None
                    player_key_list[0].use_key()

                else:
                    you_died=s.Death(w)
                    player.undraw()
                    w.after(1000)
                    you_died.undraw()
                    player=p.Player(w, 60, 360)
        
        
        
        
    if player.collision_detection(maze) == True:
        you_died=s.Death(w)
        player.undraw()
        w.after(1000)
        you_died.undraw()
        player=p.Player(w, 60, 360)
        
        
w.close()