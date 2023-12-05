

file = open("input.txt", "r")
Lines = file.readlines()
Numbers = []

for line in Lines:
    if not line.strip():
        pass
    else:
        Numbers.append(int(line.strip()))
c = 0
trips = []


for _ in range(len(Numbers)):
    if _ == 0 or _ == (len(Numbers)-1):
        pass 
    else:
        trips.append(Numbers[_-1] + Numbers[_] + Numbers[_+1])
print(trips)

for _ in range(len(trips)):
    if _ == 0:
        pass
    else:
        if (trips[_] - trips[_-1]) >0:
            c = c+1
print(c)

