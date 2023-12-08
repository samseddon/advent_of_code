import os                                                                         
import sys                                                                     
### Get the parent directory by going one level up                             
current_dir = os.path.dirname(os.path.abspath(__file__))                       
### Add the parent directory to sys.path                                       
parent_dir = os.path.dirname(current_dir)                                      
uber_parent_dir = os.path.dirname(parent_dir)
sys.path.append(uber_parent_dir)                                                    
import aoc_toolkit.equations as aoc 

def area(l, w, h):
    return l*w, w*h, h*l, l+l+w+w, w+w+h+h, h+h+l+l, 2*l*w + 2*w*h + 2*h*l

f = open("input.txt")
#f = open("test_input.txt")

Lines = f.readlines()
total_area = 0 
total_perim = 0
for line in Lines:
    if line:
        read_line_dict = aoc.line_dict(line, "{l}x{w}x{h}\n")
        l = int(read_line_dict["l"])
        w = int(read_line_dict["w"])
        h = int(read_line_dict["h"])
        output = area(l, w, h)
        total_area += min(output[:3]) + output[-1]
        #print(output)
        total_perim += int(read_line_dict["l"]) \
        * int(read_line_dict["w"]) \
        * int(read_line_dict["h"]) \
        + min(output[3:-1])

print(total_area)
print(total_perim)
#    

