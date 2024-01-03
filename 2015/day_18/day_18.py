import os                                                                      
import sys                                                                     
### Get the parent directory by going one level up                             
current_dir = os.path.dirname(os.path.abspath(__file__))                       
### Add the parent directory to sys.path                                       
parent_dir = os.path.dirname(current_dir)                                      
pparent_dir = os.path.dirname(parent_dir)                                      
sys.path.append(pparent_dir)                                                   
import aoc_toolkit.equations as aoc                                            
import pprint as pp                                                                               
import numpy as np 
from copy import deepcopy


def coord_dict_maker(coord_dict):
    for coord in all_coords:
        coord_dict = neighbour_finder(coord, size, coord_dict)
    return coord_dict

def neighbour_finder(coord, size, coord_dict):
    neighbours = []
    for x in range(3):
        for y in range(3):
            x_new = coord[0] - 1 + x
            y_new = coord[1] - 1 + y
            if x_new == coord[0] and y_new == coord[1]:
                pass
            elif x_new < 0 or y_new < 0:
                pass
            elif x_new > size -1 or y_new > size -1:
                pass
            else:
                neighbours.append((x_new, y_new))
    coord_dict[str(coord)] = neighbours
    return coord_dict

def initilise(f, garden, all_coords, fill = True):
    for y, line in enumerate(f.readlines()):
        for x, char in enumerate(line.strip()):
            all_coords.append((x,y))
            if char == "#" and fill == True:
                garden[y][x] = 1
    return garden, all_coords

def update_coords(garden, coord, coord_dict, new_garden):
    conway = sum([garden[border[1]][border[0]] for border in coord_dict[str(coord)]])
    light = garden[coord[1]][coord[0]]
    if light == 1 and 2<= conway <=3:
        new_garden[coord[1]][coord[0]] = 1
        return new_garden
    elif light == 1:
        new_garden[coord[1]][coord[0]] = 0 
        return new_garden
    if light == 0 and conway == 3:
        new_garden[coord[1]][coord[0]] = 1
        return new_garden
    elif light == 0:
        new_garden[coord[1]][coord[0]] = 0 
        return new_garden



f = open("input.txt")
#f = open("test-input.txt")
garden = []
size = 100
for y in range(size):                                                      
    temp = []                                                              
    for x in range(size):                                                  
        temp.append(0)                                                     
    garden.append(temp)
all_coords = []

garden, all_coords = initilise(f, garden, all_coords)

coord_dict = dict()
coord_dict = coord_dict_maker(coord_dict)

c = 0 
steps = 100
results = []
while c<steps:
    new_garden = deepcopy(garden)
    for coord in all_coords: 
        new_garden = update_coords(garden, coord, coord_dict, new_garden)
    results.append(sum([sum(x) for x in new_garden]))
    garden = deepcopy(new_garden)
    c += 1
print(results[-1])




