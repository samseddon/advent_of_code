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

        
places = set()
distances = dict()
for line in f.readlines():
    ld = aoc.line_dict(line, "{start} to {end} = {dist:d}\n")
    places.add(ld["start"])
    places.add(ld["end"])
    distances.setdefault(ld["start"], dict())[ld["end"]] = ld["dist"]
    distances.setdefault(ld["end"], dict())[ld["start"]] = ld["dist"]

perms_dists = []
for perm in permutations(places):
    perm_dist = 0
    for _ in range(len(perm)-1):
        start = perm[_]
        end = perm[_+1]
        perm_dist += distances[start][end]

    perms_dists.append(perm_dist)
print(min(perms_dists))
print(max(perms_dists))
