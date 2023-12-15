import os                                                                      
import sys                                                                     
### Get the parent directory by going one level up                             
current_dir = os.path.dirname(os.path.abspath(__file__))                       
### Add the parent directory to sys.path                                       
parent_dir = os.path.dirname(current_dir)                                      
uber_parent_dir = os.path.dirname(parent_dir)                                  
sys.path.append(uber_parent_dir)                                               
import aoc_toolkit.equations as aoc  
from itertools import groupby
import numpy as np
import time




line = "hepxcrrq"
line = "hepxxyzz"
#line = "abcdefgh"
#line  = "ccicci"

lowercase = aoc.lowercase()
lowercase = {char : _ for _, char in enumerate(lowercase)}
inv_lowercase = aoc.dict_inverter(lowercase)

con_letters = []
for _ in range(len(aoc.lowercase())-2):
    con_letters.append(aoc.lowercase()[_] + aoc.lowercase()[_+1] + aoc.lowercase()[_+2])

def incrementer(s):
    '''I've only just met 'er!'''
    last_char = s[-1]
    if last_char == "z":
        new_last_char = "a"
        s = incrementer(s[:-1])
        return s + new_last_char
    else:
        new_last_char = inv_lowercase[lowercase[last_char] + 1]
        return s[:-1] + new_last_char 

def double_letter(s):
    keys = []
    groups = []
    for key, group in groupby(s):
        if len(list(group)) > 1:
             keys.append(key)
    if len(np.unique(keys)) > 1:
            return True, s
    else:
        return False, s

def naughty_letters(s):
    letters = ["i", "o", "l"]
    for letter in letters:
        if letter in s:
            app_string = ""
            for _ in range(len(s)-s.index(letter)-1):
                app_string += "a"
            
            return False, s#  s[:s.index(letter)] + inv_lowercase[lowercase[letter] + 1] + app_string

    return True, s

def consec_letters(s):
    for l_s in con_letters:
        if l_s in s:
            return True, s
    return False, s

def remove_naughty(s):
    letters = ["i", "o", "l"]
    for letter in letters:
        if letter in s:
            app_string = ""
            for _ in range(len(s)-s.index(letter)-1):
                app_string += "a"
            return s[:s.index(letter)] + inv_lowercase[lowercase[letter] + 1] + app_string


def tester(s):
    nl_bool, s = naughty_letters(s)
    if nl_bool == False:
        s = remove_naughty(s)
        nl_bool, s = naughty_letters(s)
    dl_bool, s = double_letter(s)
    cn_bool, s = consec_letters(s) 
    if nl_bool == True and dl_bool == True and cn_bool == True:

        return True, s
    else:
        return False, s
    #    #Do some things!
    #    return tester(s)
    #elif:
    #return 1 

line = incrementer(line)

pass_test = False

while pass_test == False:
    pass_test, line = tester(line)
    if pass_test == True:
        break
    else:
        line = incrementer(line)
 
print(line)
