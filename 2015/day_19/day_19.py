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
swap = Swaps[0]
print(swap)
# will loop over this
results = set()
for swap in Swaps:
    for thing in re.finditer(swap["sour"], seed):
        results.add(seed[:thing.span()[0]]+ swap["repl"] + seed[thing.span()[1]:])

print(len(results))
