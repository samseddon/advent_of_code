import os                                                                      
import sys                                                                     
### Get the parent directory by going one level up                             
current_dir = os.path.dirname(os.path.abspath(__file__))                          
### Add the parent directory to sys.path                                          
parent_dir = os.path.dirname(current_dir)                                      
uber_parent_dir = os.path.dirname(parent_dir)                                     
sys.path.append(uber_parent_dir)                                                  
import aoc_toolkit.equations as aoc   

import re


if __name__ == "__main__":
    f = open("input.txt")
    #f = open("test-input.txt")
    Lines = f.readlines()
    abs_line_len = []
    act_line_len = []
    count1 = 0 
    count2 = 0 
    count3 = 0
    for line in Lines:
        print(line)
        print(eval(line))
        count1 += len(line.strip())
        count2 += len(eval(line))
        quotes = line.strip().count('"')
        backsl = line.strip().count('\\')
        print(len(line.strip()) +  quotes +  backsl + 2)
        count3 += (len(line.strip()) +  quotes + backsl + 2)
    print(count3- count1)
