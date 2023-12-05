from functools import reduce


class Game:

    def __init__(self, index, cubes_shown):
        self.index = index
        self.cubes_shown = cubes_shown.split(";")
        self.maxes = {"red" : 0, 
                    "green" : 0, 
                     "blue" : 0}
        self.separate_games()
     

    def separate_games(self):
        for cubes in self.cubes_shown:
            cubes = cubes.split(", ")
            for hand in cubes:
                hand = hand.split(" ")
                if int(hand[-2]) > int(self.maxes[hand[-1]]):
                    self.maxes[hand[-1]] = int(hand[-2])

    def power(self):
        power = []
        for key in self.maxes:
            print(self.maxes[key])
            power.append(int(self.maxes[key]))

        return reduce(lambda x, y: x*y, power)
        
    


f = open("test-input.txt")
f = open("input.txt")
Lines = f.readlines()
Results = []

for line in Lines:
    index = int(line.strip().split(":")[0][5:])
    cubes_shown = line.strip().split(":")[1]
    game = Game(index, cubes_shown)
    Results.append(game.power())
final_result = 0
for result in Results:
    final_result += result

print(final_result)
