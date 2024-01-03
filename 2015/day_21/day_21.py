import os                                                                      
import sys                                                                     
### Get the parent directory by going one level up                             
current_dir = os.path.dirname(os.path.abspath(__file__))                       
### Add the parent directory to sys.path                                       
parent_dir = os.path.dirname(current_dir)                                      
uber_parent_dir = os.path.dirname(parent_dir)                                  
sys.path.append(uber_parent_dir)                                               

import aoc_toolkit.equations as aoc      
from itertools import permutations
import math


f = open("shop.txt")
weapons = {}
armors = {}
rings = {}
val = 0 
_ = 0 
for line in f.readlines():
    if not line.strip():
        val += 1
    elif val == 0:
        if "Weapons" in line:
            pass 
        else:
            line = line.split()
            weapons[line[0]] = {"name" : line[0], 
                          "cost" : line[1], 
                          "dama" : line[2],
                          "armo" : line[3]}
            _+= 1
    elif val == 1:
        if "Armor" in line:
            pass 
        else:
            line = line.split()
            armors[line[0]] =  {"name" : line[0], 
                          "cost" : line[1], 
                          "dama" : line[2],
                          "armo" : line[3]}
            _+= 1
    elif val == 2:
        if "Rings" in line:
            pass 
        else:
            line = line.split()
            rings[line[0]] =   {"name" : line[0], 
                          "cost" : line[1], 
                          "dama" : line[2],
                          "armo" : line[3]}
            _+= 1

armors["none"] = {"name": "none", "cost":0, "dama":0, "armo":0}
rings["none"] = {"name": "none", "cost":0, "dama":0, "armo":0}
rings["none2"] = {"nam2": "none", "cost":0, "dama":0, "armo":0}
print(len(armors))

boss = {}
boss["hits"] = 104
boss["dama"] = 8
boss["armo"] = 1
hits = 100
total_cost = []
for weapon in weapons.values():
    for armor in armors.values():
        for ring1 in rings.values():
            for ring2 in rings.values():
                dama = int(weapon["dama"]) + int(ring1["dama"]) + int(ring2["dama"])
                armo = int(armor["armo"]) + int(ring1["armo"]) + int(ring2["armo"])
                if ring1 == ring2:
                    pass
                else :
                    try:
                        check1 =  math.ceil(boss["hits"] / max((dama-boss["armo"], 1)))
                        check2 = math.ceil(hits/max((boss["dama"]-armo), 1))
                        if check1 > check2:
                            total_cost.append(int(weapon["cost"]) + int(armor["cost"]) + int(ring1["cost"]) + int(ring2["cost"]))
                            if total_cost[-1] == 91:
                                print(weapon, armor, ring1, ring2)
                    except:
                        ZeroDivisionError

print(max(total_cost))




