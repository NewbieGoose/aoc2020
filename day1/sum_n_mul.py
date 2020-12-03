#!/usr/bin/env python3

import sys
        

# Assume that there exist two numbers which sum to CONST
if __name__ == "__main__":
    FILENAME = 'input.txt'
    CONST = 2020
    if len(sys.argv) > 1:
        FILENAME = sys.argv[1]
    
    with open(FILENAME) as inp:
        data  = sorted([int(x) for x in inp.readlines()])
    
    start = 0
    end = len(data) - 1
    s = data[end] + data[start]

    while s != CONST:
        print(s)
        if s > CONST:
            end -= 1
        else:
            start += 1
        s = data[start] + data[end]
    
    print(f'{data[start]} + {data[end]} = {s}')
    print(f'{data[start]} * {data[end]} = {data[end]*data[start]}')
    