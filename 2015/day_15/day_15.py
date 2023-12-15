import os
import sys
### Get the parent directory by going one level up
current_dir = os.path.dirname(os.path.abspath(__file__))
### Add the parent directory to sys.path
parent_dir = os.path.dirname(current_dir)
uber_parent_dir = os.path.dirname(parent_dir)
sys.path.append(uber_parent_dir)
import aoc_toolkit.equations as aoc


f = open("input.txt")
#f = open("test-input.txt")

props = set()
ingr = []

calo = []
for line in f.readlines():
    pattern = "{name}: capacity {capa:d}, durability {dura:d}, flavor {flav:d}, texture {text:d}, calories {calo:d}\n"
#    pattern = "{name}: capacity {capa:d}, durability {dura:d}, flavor {flav:d}, texture {text:d}\n"
    ld = aoc.line_dict(line, pattern)
    name = ld["name"]
    del ld["name"]
    calo.append(ld["calo"])
    del ld["calo"]
    ingr.append(ld)
print(calo)    


for key in ingr[-1].keys():
    props.add(key)

all_poss = []
for i in range(101):
    for j in range(101-i):
        for k in range(101-i - j):
            l = 100 - i - j - k
            all_poss.append([i, j, k, l])

#for i in range(101):
#    j = 100- i
#    all_poss.append([i, j])
all_totals = []

print(ingr)

#all_poss = [[44,56]]
trying_circs = []
for n in all_poss:
    total = 1
    for prop in props:
        print(prop)
        value = 0
        for _ in range(len(n)):
            temp = n[_] * ingr[_][prop]
            value += temp
        print(value)
        if value > 0:
            total *= value
        else:
            total *= 0
    all_totals.append(total)
    cal_val = 0 
    for _ in range(len(n)):
        cal_val += n[_] * calo[_]
    if cal_val == 500:
        trying_circs.append(total)
        print("cal_val")
print(max(all_totals), max(trying_circs))
