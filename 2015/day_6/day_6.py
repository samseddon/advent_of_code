import os                                                                         
import sys
### Get the parent directory by going one level up
current_dir = os.path.dirname(os.path.abspath(__file__))
### Add the parent directory to sys.path
parent_dir = os.path.dirname(current_dir)
pparent_dir = os.path.dirname(parent_dir)
sys.path.append(pparent_dir)                                                    
import aoc_toolkit.equations as aoc  

import numpy as np


if __name__ == "__main__":
    f = open("input.txt")
    #f = open("test-input.txt")
    Lines = f.readlines()
    

    garden = []
    size = 10000
    for y in range(size):
        temp = []
        for x in range(size):
            temp.append(0)
        garden.append(temp)
         
    
    for line in Lines:
        line = line.strip()
        line = line.split(" ")
        end = line[-1].split(",")
        start = line[-3].split(",")
        x_start = int(start[0])
        y_start = int(start[1])
        x_end   = int(end[0])
        y_end   = int(end[1])
        for x in range(x_start, x_end+1, 1):
            for y in range(y_start, y_end+1, 1):
                if line[0] == "toggle":
                    if garden[x][y] == 1:
                        garden[x][y] = 0
                    else:
                        garden[x][y] = 1
                else:
                    if line[1] == "on":
                        garden[x][y] = 1
                    elif line[1] == "off":
                        garden[x][y] = 0 
    garden = np.array(garden)
    print(np.sum(garden))
