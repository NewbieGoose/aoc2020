#!/usr/bin/env python3

import sys

TREE = '#'
FREE = '.'

DIRECTION_H = 3
# DIRECTION_V = 1

if __name__ == "__main__":
    FILENAME = 'input.txt'
    if len(sys.argv) > 1:
        FILENAME = sys.argv[1]
    
    with open(FILENAME) as inp:
        terrain  = [line.strip() for line in inp.readlines()]
    
    pos_x = 0
    tree_counter = 0
    for row in terrain[1:]:
        pos_x += DIRECTION_H
        tree_counter += 1 if row[pos_x%len(row)] == TREE else 0
    print(tree_counter)

    