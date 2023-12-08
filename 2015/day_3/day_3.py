import os                                                                      
import sys                                                                     
### Get the parent directory by going one level up                             
current_dir = os.path.dirname(os.path.abspath(__file__))                          
### Add the parent directory to sys.path                                          
parent_dir = os.path.dirname(current_dir)                                      
uber_parent_dir = os.path.dirname(parent_dir)                                     
sys.path.append(uber_parent_dir)                                                  
import aoc_toolkit.equations as aoc  


if __name__ == "__main__":
    f = open("input.txt")
    #f = open("test-input.txt")
    Line = f.readline()
    Line = Line.strip()
    positions = []
    position_1 = (0,0)
    position_2 = (0,0)
    positions.append(position_1)
    positions.append(position_2) 
    for _, char in enumerate(Line):
        if _ % 2 == 0:
            if char == "^":
                position_1 = (position_1[0], position_1[1] + 1)
            if char == ">":
                position_1 = (position_1[0] + 1, position_1[1])
            if char == "v":
                position_1 = (position_1[0], position_1[1] - 1)
            if char == "<":
                position_1 = (position_1[0] - 1, position_1[1])
            positions.append(position_1)
        else:
            if char == "^":
                position_2 = (position_2[0], position_2[1] + 1)
            if char == ">":
                position_2 = (position_2[0] + 1, position_2[1])
            if char == "v":
                position_2 = (position_2[0], position_2[1] - 1)
            if char == "<":
                position_2 = (position_2[0] - 1, position_2[1])
            positions.append(position_2)
    


    print(len(list(set(positions))))
