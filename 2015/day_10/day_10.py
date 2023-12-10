from itertools import groupby

line = "3113322113"
counter = 0
reduced_x = []
reduced_y = []
c=0

groups = []
number = []


def look_and_say(line):
    new_line = ""    
    for key, group in groupby(line):
        char = list(group)
        new_line += str(len(char)) + char[0]
    return new_line
c=0
while c<50:
    line = look_and_say(line)
    c+=1
print(len(line))
