

def vowel(line):
    c = 0 
    for char in line:
        if "a" == char:
            c += 1
        if "e" == char:
            c += 1
        if "i" == char:
            c += 1
        if "o" == char:
            c += 1
        if "u" in char:
            c += 1
    if c<3:
        return False

def double(line):
    c = 0 
    for char in line:
        if char + char in line:
            c+=1
    if c == 0:
        return False
    

if __name__ == "__main__":
    f = open("input.txt")
    #f = open("test-input.txt")
    Lines = f.readlines()
    nice = []
    for line in Lines:
        line = line.strip()
        if vowel(line) == False:
            pass
        elif double(line) == False:
            pass

        elif "ab" in line or\
             "cd" in line or\
             "pq" in line or\
             "xy" in line:
            pass
        else:
            nice.append(line)
    print(nice)
    print(len(nice))
                     

