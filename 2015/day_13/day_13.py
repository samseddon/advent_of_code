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

f = open("input.txt")
#f = open("test-input.txt")
people = set()
seating_arrangement = dict()

for line in f.readlines():
    pattern = "{name} would {sign} {amount:d} happiness units by sitting next to {partner}.\n"
    ld = aoc.line_dict(line, pattern)
    if ld["sign"] == "lose":
        ld["amount"] *= -1
    people.add(ld["name"])
    seating_arrangement.setdefault(ld["name"], dict())[ld["partner"]] \
                                                     = ld["amount"]
for key in people:
    seating_arrangement[key]["Sam"] = 0 
    seating_arrangement.setdefault("Sam", dict())[key] \
                                                     = 0
people.add("Sam")
print(seating_arrangement)
happiness_ratings = []
for perm in permutations(people):
    print(perm)
    rating = 0
    for _ in range(len(perm)-1):
        rating += seating_arrangement[perm[_]][perm[_+1]]
        rating += seating_arrangement[perm[_+1]][perm[_]]
    rating += seating_arrangement[perm[-1]][perm[0]]
    rating += seating_arrangement[perm[0]][perm[-1]]
    happiness_ratings.append(rating)
print(max(happiness_ratings))
        

