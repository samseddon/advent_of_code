import numpy as np
from itertools import combinations

f = open("input.txt")
containers = []
unsorted = []
amount = 150
for _, line in enumerate(f.readlines()):
    containers.append(int(line.strip()))
print(containers)

total = []

for _ in range(0, len(containers)+1):
    test = len([poss_containers for poss_containers in combinations(containers, _) \
            if sum(poss_containers) == amount])
    print(test)
    if test > 0:
        total.append(test)
print(sum(total), min(total))
