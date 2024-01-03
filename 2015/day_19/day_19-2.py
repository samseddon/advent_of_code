import os                                                                      
import sys                                                                     
### Get the parent directory by going one level up                             
current_dir = os.path.dirname(os.path.abspath(__file__))                       
### Add the parent directory to sys.path                                       
parent_dir = os.path.dirname(current_dir)                                      
pparent_dir = os.path.dirname(parent_dir)                                      
sys.path.append(pparent_dir)                                                   
import aoc_toolkit.equations as aoc                                            
                                       
import re
from copy import deepcopy

f = open("input.txt")
#f = open("test-input.txt")
Lines = f.readlines()
pattern = "{sour} => {repl}\n"
Swaps = []
for _, line in enumerate(Lines):
    if not line.strip():
        pass
    elif _ == len(Lines)-1:
        seed = line.strip()
    else:
        Swaps.append(aoc.line_dict(line, pattern))
# will loop over this
sorted_Swaps= sorted(Swaps, key=lambda x: -len(x["repl"]))
new_seed = deepcopy(seed)
c= 0 
print(seed)
while seed != "e":
    for swap in sorted_Swaps:
        # confusingly a simple replace works by sorting from largest to small
        # in line 27. Not very nice solution but reddit suggested it was poss
        # and the alternative is long and shit..
        if swap["repl"] in seed:
            seed = seed.replace(swap["repl"], swap["sour"],1 )
            c += 1
        
print(c)
