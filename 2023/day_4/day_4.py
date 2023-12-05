import os
import sys
# Get the parent directory by going one level up
current_dir = os.path.dirname(os.path.abspath(__file__))
# Add the parent directory to sys.path
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
import aoc_toolkit.equations as aoc

import numpy as np


if __name__ == "__main__":
    f = open("test-input.txt")
    #f = open("input.txt")
    Lines = f.readlines()
    pattern = "Card {card:d}: {winners} | {hand}\n"

    for line in Lines:
        line = aoc.line_dict(line, pattern)
        winners = aoc.int_array(line, "winners")
        hand = aoc.int_array(line, "hand")
        print(int(np.floor(0.5 * 2**(len(set(winners) & set(hand))))))
