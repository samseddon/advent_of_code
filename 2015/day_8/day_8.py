import os                                                                      
import sys                                                                     
### Get the parent directory by going one level up                             
current_dir = os.path.dirname(os.path.abspath(__file__))                          
### Add the parent directory to sys.path                                          
parent_dir = os.path.dirname(current_dir)                                      
uber_parent_dir = os.path.dirname(parent_dir)                                     
sys.path.append(uber_parent_dir)                                                  
import aoc_toolkit.equations as aoc   

import re


if __name__ == "__main__":
    f = open("input.txt")
    f = open("test-input.txt")
    Lines = f.readlines()
    abs_line_len = []
    act_line_len = []
    for line in Lines:
        length = 0
        line = line.strip()
        print(line)
        abs_line_len.append(len(line))
        line = line[1:-1]
        skipper = 0
        for _ in range(0, len(line)-1):
            _ = skipper+_
            if _ == len(line)-1:
                length += 1
                break
            elif _ > len(line)-1:
                break
            
            elif line[_] == "\\":
                if line[_+1] == "x":
                    s = line[_+2:_+4]
                    #print("u'"+s+"'")
                    #s = s.encode("utf-8")
                    int(s, base=16)
                    byte_string = bytes.fromhex(s) 
                    ascii_string = byte_string.decode("ASCII")
                    print(ascii_string)
                    #print(len(ascii_string))
                    #length += len(ascii_string)
                    print(length)
                    skipper +=3
                    pass
                else:
                    print("some random escape")
                    length += 1
                    skipper += 2
            else:
                "normal escape"
                length += 1
                if _ == len(line)-2:
                    length+=1
        act_line_len.append(length)
        #line = line.encode("utf-8")
        #byte_string = bytes.fromhex(line)
        #ascii_string = byte_string.decode("ASCII")  
        #print(ascii_string)
    print(abs_line_len, act_line_len) 
    print(sum(abs_line_len) - sum(act_line_len)) 
