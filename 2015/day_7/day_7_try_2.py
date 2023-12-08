import os                                                                      
import sys                                                                     
### Get the parent directory by going one level up                             
current_dir = os.path.dirname(os.path.abspath(__file__))                          
### Add the parent directory to sys.path                                          
parent_dir = os.path.dirname(current_dir)                                      
uber_parent_dir = os.path.dirname(parent_dir)                                     
sys.path.append(uber_parent_dir)                                                  
import aoc_toolkit.equations as aoc 

#def query_value(wire, network):
#     
#    if network[wire].has_value == True:
#        return network
#    elif network[wire].op == "NOT" \
#            or network[wire].op == "LSHIFT"\
#            or network[wire].op == "RSHIFT"\
#            or network[wire].op == "REPLACE":
#        print("here")
#        updated_network = query_value(network[wire].in_1, network)
#        updated_network[wire].update_value(updated_network)
#        return updated_network
#    else:
#        updated_network = query_value(network[wire].in_1, network)
#        updated_network = query_value(network[wire].in_2, updated_network)
#        updated_network[wire].update_value(updated_network)
#        #print(wire, updated_network[wire].value)
#        return updated_network
#    
#
#
#        
#
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
            self.value = int(network[self.in_1])
            self.has_value = True
        if self.op == "AND":
            self.value = int(network[self.in_1]) & int(network[self.in_2])
            self.has_value = True
        if self.op == "OR":
            self.value = int(network[self.in_1]) | int(network[self.in_2])
            self.has_value = True
        if self.op == "LSHIFT":
            self.value = int(network[self.in_1]) << int(self.in_2)
            self.has_value = True
        if self.op == "RSHIFT":
            self.value = int(network[self.in_1]) >> int(self.in_2)
            self.has_value = True
        if self.op == "NOT":
            self.value = int(network[self.in_1]) ^ 65535
            self.has_value = True


if __name__ == "__main__":
     
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
    values = {}
    #while len(values) < len(network):
    c=0 
    while c<10**5:
        for wire in network:
            if network[wire].has_value == True:
                values[wire] = network[wire].value
            else:
                try:
                    network[wire].update_value(values)
                except:
                    KeyError
        c+=1
    print(values)
