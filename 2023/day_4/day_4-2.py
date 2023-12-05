import os
import sys
# Get the parent directory by going one level up
current_dir = os.path.dirname(os.path.abspath(__file__))
# Add the parent directory to sys.path
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
import aoc_toolkit.equations as aoc

import numpy as np
from collections import OrderedDict
import pprint as pp


if __name__ == "__main__":
    f = open("test-input.txt")
    f = open("input.txt")
    Lines = f.readlines()
    pattern = "Card {card}: {winners} | {hand}\n"
    Originals = {}
    for line in Lines:
        line = aoc.line_dict(line, pattern)
        card = line["card"]
        winners = aoc.int_array(line, "winners")
        hand = aoc.int_array(line, "hand")
        Originals[int(card)] = [int(card) + i + 1 
                          for i in 
                          range(len(set(winners) & set(hand)))]
    Copies = {}
    #Originals = OrderedDict(sorted(Originals.items(), key=lambda t: t[0]))
    total_cards = {}
    
    for key in Originals:
        for card in Originals[key]:
            if card in Copies.keys():
                Copies[card] += 1
            else:
                Copies[card] = 1
    print(Copies)
    card_counter = {} 
    for key in Originals.keys():
        card_counter[key] = 1
        if key in Copies.keys():
            card_counter[key] = card_counter[key] + Copies[key]

            for card in Originals[key]:
                Copies[card] += Copies[key]

    print(sum(card_counter.values()))
