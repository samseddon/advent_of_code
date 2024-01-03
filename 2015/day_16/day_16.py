import os                                                                      
import sys                                                                     
### Get the parent directory by going one level up                             
current_dir = os.path.dirname(os.path.abspath(__file__))                       
### Add the parent directory to sys.path                                       
parent_dir = os.path.dirname(current_dir)                                      
uber_parent_dir = os.path.dirname(parent_dir)                                  
sys.path.append(uber_parent_dir)                                               
import aoc_toolkit.equations as aoc

import ast 

class big_suze():
    def __init__(self, number):
        self.num = int(number)
        self.children = None
        self.cats = None
        self.samoyeds = None
        self.pomeranians = None
        self.akitas = None
        self.vizslas = None
        self.goldfish = None
        self.trees = None
        self.cars = None
        self.perfumes = None

    def add_traits(self, things):
        for thing in things[self.num].keys():
            setattr(self, thing, things[self.num][thing])

def compare(sue1, sue2):
    for item in vars(sue2).items():
        if item[0] == "num":
            pass
        elif item[1] == None:
            pass
        elif item[1] != vars(sue1)[item[0]]:
   #         print(item[0], item[1], vars(sue1)[item[0]])
            return 1
    print("This is the sue:", sue2.num)
    return 0

def part2_compare(sue1, sue2):
    for item in vars(sue2).items():
        if item[0] == "num":
            pass
        elif item[1] == None:
            pass
        elif item[0] == "cats" or item[0] == "trees":
            if item[1] < vars(sue1)[item[0]]:
                return 1
        elif item[0] == "pomeranians" or item[0] == "goldfish":
            print(item[0], item[1], vars(sue1)[item[0]])
            
            if item[1] > vars(sue1)[item[0]]:

                return 1
        elif item[1] != vars(sue1)[item[0]]:
   #         print(item[0], item[1], vars(sue1)[item[0]])
            return 1
    print("This is the sue:", sue2.num)
    return 0

f = open("input.txt")
pattern = "Sue {num:d}: {items}\n"
things = dict()
Sues = []
master_sue_anal = {0:{"children": 3,
                      "cats": 7,
                      "samoyeds": 2,
                      "pomeranians": 3,
                      "akitas": 0,
                      "vizslas": 0,
                      "goldfish": 5,
                      "trees": 3,
                      "cars": 2,
                      "perfumes": 1}}


master_sue = big_suze(0)
master_sue.add_traits(master_sue_anal)


for line in f.readlines():
    ld = aoc.line_dict(line, pattern)
    Sues.append(big_suze(ld["num"]))
    for thing in ld["items"].split(","):
        thing_s = thing.split(":")
        things.setdefault(ld["num"], dict())[str(thing_s[0]).strip()] = int(thing_s[1])

for sue in Sues:
    sue.add_traits(things)
    part2_compare(master_sue, sue)

