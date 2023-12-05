

class Part:
    def __init__(self, number_1, line_number, row_number):
        self.is_part = False
        self.value = number_1
        self.seed_coordiante = (line_number, row_number)
        self.coordinates = []
        self.coordinates.append((line_number, row_number))
        self.extra_coords = []

    def add_digit(self, val, line, row):
        self.value += val
        self.coordinates.append((line,row))

    def influencer(self):
        for coord in self.coordinates:
            for i in range(3):
                i = i-1
                for j in range(3):
                    j = j-1
                    if i == 0 and j == 0:
                        pass
                    else:
                        self.extra_coords.append((coord[0]+i, coord[1]+j))


    def combiner(self):
        self.bubble_coords = []
        for coord in self.extra_coords:
            if coord in self.coordinates:
                pass
            else:
                self.bubble_coords.append(coord)
        self.unique_coords = list(set(self.bubble_coords))

    def checker(self, symbols):
        return (len(set(self.unique_coords) & set(symbols)))


if __name__ == "__main__":
    f = open("test-input.txt")
    #f = open("input.txt")
    Lines = f.readlines()
    Parts = []
    symbols = [] 
    for i, line in enumerate(Lines): 
        last_thing_was_dot = True
        number_line = []
        line = line.strip()
        for j, char in enumerate(line):
            if char == ".":
                last_thing_was_dot = True
                pass
            elif char.isalnum() == False:
                symbols.append((i,j))
                last_thing_was_dot = True
            else:
                int(char)
                if last_thing_was_dot == True:
                    Parts.append(Part(char, i, j))
                    last_thing_was_dot = False
                else:
                    Parts[-1].add_digit(char, i, j)
        last_thing_was_dot = True 
    parts_summed = 0

    for part in Parts:
        #for coord in part.coordinates:
        #    symbols.append(coord)
        part.influencer()
        part.combiner()
        if part.checker(symbols) == 1:
            parts_summed += int(part.value)
        
    print(parts_summed) 
