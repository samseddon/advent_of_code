import os                                                                      
import sys                                                                     
### Get the parent directory by going one level up                             
current_dir = os.path.dirname(os.path.abspath(__file__))                       
### Add the parent directory to sys.path                                       
parent_dir = os.path.dirname(current_dir)                                      
uber_parent_dir = os.path.dirname(parent_dir)                                  
sys.path.append(uber_parent_dir)                                               
import aoc_toolkit.equations as aoc



class Reindeer():
    def __init__(self, ld):
        self.name = ld["name"]
        self.speed = ld["speed"]
        self.stamina = ld["time"]
        self.rest = ld["rest"]
        self.resting_status = False
        self.time_left = self.stamina + 1 
        self.distance = 0
        self.points = 0

    def update_time(self):
        self.time_left -= 1
        if self.time_left == 0 and self.resting_status == False:
            self.resting_status = True
            self.time_left = self.rest
            pass
        elif self.time_left == 0 and self.resting_status == True:
            self.resting_status = False
            self.time_left = self.stamina 
            pass
        if self.resting_status == False:
            self.distance += self.speed
        else:
            pass
    
    def add_point(self):
        self.points += 1
    
            
f = open("input.txt")

#f = open("test-input.txt")
Reindeers = dict()
for line in f.readlines():
    ld = aoc.line_dict(line, "{name} can fly {speed:d} km/s for {time:d}" \
            + " seconds, but then must rest for {rest:d} seconds.\n")
    Reindeers[ld["name"]] = Reindeer(ld)
time = 1
print(Reindeers)
#reindeer = Reindeers["Comet"]
max_dist = 0
while time:
    for reindeer in Reindeers.values():
        reindeer.update_time()
        if reindeer.distance > max_dist:
            max_dist = reindeer.distance
    for reindeer in Reindeers.values():
        if reindeer.distance == max_dist:
            reindeer.add_point()
    time += 1
    if time > 2503:
        break
names = []
final_distances = []
for reindeer in Reindeers.values():
    print(reindeer.name, reindeer.points)
    final_distances.append(reindeer.points)
    names.append(reindeer.name)

print(max(final_distances))

