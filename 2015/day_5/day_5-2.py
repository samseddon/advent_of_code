

def rule1(line):
    c = 0 
    for char in line:
        print(char)
        if line.count(char)>1:
            pos = [pos for pos, c in enumerate(line) if c == char]
            print(pos)
            for _ in range(1, len(pos)):
                if pos[_] - pos[_-1] > 1:
                    c += 1
                
    if c == 0:
        return False

def rule2(line):
    c = 0 
    for _ in range(0, len(line)-2, 1):
        if line[_] == line[_+2]:
            c += 1
            print("YES")
    if c == 0:
        return False

if __name__ == "__main__":
    f = open("input.txt")
    f = open("test-input.txt")
    Lines = f.readlines()
    nice = []
    for line in Lines:
        line = line.strip()
        if rule1(line) == False:
            pass
        elif rule2(line) == False:
            pass

        else:
            nice.append(line)
    
    print(nice)
    print(len(nice))
                     

