

f = open("input.txt")
line = f.readline().strip()

floor = 0 

for _, char in enumerate(line):
    if char == "(":
        floor += 1
    else:
        floor -= 1
    if floor == -1:
        print(_+1)

