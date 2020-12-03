#!/usr/bin/env python3

import sys
from functools import reduce

TREE = '#'
FREE = '.'

def tree_counter(terrain, slope):
    slope_x, slope_y = slope
    pos_y, pos_x = (0,0)
    counter = 0
    row_len = len(terrain[0])
    while pos_y != len(terrain) - 1:
        pos_x += slope_x
        pos_y += slope_y
        true_y = min(pos_y, len(terrain))
        true_x = pos_x % row_len
        counter += 1 if terrain[true_y][true_x] == TREE else 0
    
    return counter

if __name__ == "__main__":
    FILENAME = 'input.txt'
    if len(sys.argv) > 1:
        FILENAME = sys.argv[1]

    slopes = [
        (1,1),
        (3,1),
        (5,1),
        (7,1),
        (1,2)
    ]
    
    with open(FILENAME) as inp:
        terrain  = [line.strip() for line in inp.readlines()]
    l = [tree_counter(terrain, slope) for slope in slopes]
    print(l)
    mul = reduce(lambda x,y:x*y,l,1)
    print(mul)

    