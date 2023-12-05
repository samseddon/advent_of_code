class Game:
    def __init__(self, et, index, cubes_shown):
        self.elf_test = et
        self.index = index
        self.cubes_shown = cubes_shown.split(";")
        self.separate_games()

    def separate_games(self):
        for cubes in self.cubes_shown:
            cubes = cubes.split(", ")
            for hand in cubes:
                hand = hand.split(" ")
                if int(hand[-2]) > int(self.elf_test[hand[-1]]):
                    return False
        return True
        
    
elf_test = {"red" : 12, 
          "green" : 13, 
           "blue" : 14}


f = open("test-input.txt")
f = open("input.txt")
Lines = f.readlines()
Results = []

for line in Lines:
    index = int(line.strip().split(":")[0][5:])
    cubes_shown = line.strip().split(":")[1]
    game = Game(elf_test, index, cubes_shown)
    Results.append((index, game.separate_games()))
final_result = 0
for result in Results:
    if result[1] == True:
        final_result += int(result[0])

print(final_result)
