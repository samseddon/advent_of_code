

file = open("input.txt", "r")
Lines = file.readlines()
Numbers = []

for line in Lines:
    if not line.strip():
        pass
    else:
        Numbers.append(int(line.strip()))
c = 0
for _ in range(len(Numbers)):
    if _ == 0:
        pass
    else: 
        if (Numbers[_] - Numbers[_-1]) >0:
            c = c+1
print(c)
        
