import os                                                                      
import sys                                                                     
### Get the parent directory by going one level up                             
current_dir = os.path.dirname(os.path.abspath(__file__))                          
### Add the parent directory to sys.path                                          
parent_dir = os.path.dirname(current_dir)                                      
uber_parent_dir = os.path.dirname(parent_dir)                                     
sys.path.append(uber_parent_dir)                                                  
import aoc_toolkit.equations as aoc 
import time

#'class Network():
#'    def __init__(self, operators):
#'        self.operators = operators 
#'        self.Wires = {}
#'    
#'    def clean_network(self):
#'        for wire in self.Wires:
#'            value = self.Wires[wire]
#'            if value.isnumeric() == True:
#'                self.Wires[wire] = int(value)
#'            else "AND" in value:
#'                value = value.split(" ")
#'                print(value)
#'                self.Wires[wire] = value[0] + "&" + value[1]
#'
#'
#'    def print_netwrok(self):
#'        for wire in self.Wires:
#'            print(wire, self.Wires[wire])
#'

class Wire():
    def __init__(self, operators, name, real, num):
        self.num = num
        self.operators = operators
        self.has_value = False
        self.name = name
        self.real = real
        self.value = None
        self.op = None

    def clean_up(self):
        if self.real.isnumeric() == True:
            self.value = int(self.real)
            self.has_value = True
        
        else:
            self.function = self.real.split(" ")
            if len(self.function) == 1:
                self.op = "REPLACE"
                self.in_1 = self.function[0]
            elif len(self.function) == 3:
                self.in_1 = self.function[0]
                self.op = self.function[1]
                self.in_2 = self.function[2]
            else:
                self.in_1 = self.function[1]
                self.op = self.function[0]

    def update_value(self, network):
        if self.op == "REPLACE":
            self.value = int(network[self.in_1].value)
            self.has_value = True
        if self.op == "AND":
            if self.in_1.isnumeric():
                val1 = int(self.in_1)
            else:
                val1 = int(network[self.in_1].value)
            if self.in_2.isnumeric():
                val2 = int(self.in_2)
            else:
                val2 = int(network[self.in_2].value)
            self.value = val1 & val2
            self.has_value = True
        if self.op == "OR":
            self.value = int(network[self.in_1].value) | int(network[self.in_2].value)
            self.has_value = True
        if self.op == "LSHIFT":
            self.value = int(network[self.in_1].value) << int(self.in_2)
            self.has_value = True
        if self.op == "RSHIFT":
            self.value = int(network[self.in_1].value) >> int(self.in_2)
            self.has_value = True
        if self.op == "NOT":
            self.value = int(network[self.in_1].value) ^ 65535
            self.has_value = True


def query_value(wire, network):
    if network[wire].has_value == True:
        return network
    elif network[wire].op == "NOT" \
            or network[wire].op == "LSHIFT"\
            or network[wire].op == "RSHIFT"\
            or network[wire].op == "REPLACE":
        updated_network = query_value(network[wire].in_1, network)
        updated_network[wire].update_value(updated_network)
        return updated_network
    else:
        if network[wire].in_1.isnumeric():
            updated_network = network
        else:
            updated_network = query_value(network[wire].in_1, network)
        if network[wire].in_2.isnumeric():
            pass
        else:
            updated_network = query_value(network[wire].in_2, updated_network)
        updated_network[wire].update_value(updated_network)
        return updated_network
    


        

if __name__ == "__main__":
    time_s = time.time()
    operators = {"AND":"&",	
                 "OR":"|",	
                 "XOR":"^",	
                 "NOT":"~",	
                 "LSHIFT":"<<", 	
                 "RSHIFT":">>"}
    f = open("input.txt")
    #f = open("test-input.txt")
    Lines = f.readlines()
    network = {}
    
    for _, line in enumerate(Lines):
        line_dict = aoc.line_dict(line, "{input} -> {name}\n")
        network[line_dict["name"]] = Wire(operators,\
                                                 line_dict["name"],\
                                                 line_dict["input"],
                                                 _)
        network[line_dict["name"]].clean_up()

    for wire in network:
        if wire == "b":
            network[wire].value = 3176
    for wire in network:
        network = query_value(wire, network)

    for wire in network:
        if wire == "a":
            print(wire, network[wire].value)
    
    print(time.time() - time_s)
    
