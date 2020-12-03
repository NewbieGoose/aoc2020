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
    
    
    dims = len(data)
    for i in range(dims):
        for j in range(dims):
            if j == i:
                continue
            elif data[i] + data[j] > CONST:
                break
            for k in range(dims):
                if k == i or k == j:
                    continue
                elif data[i] + data[j] + data[k] > CONST:
                    break
                if data[i] + data[j] + data[k] == CONST:
                    print(f'{data[i]} + {data[j]} + {data[k]} = {data[i]+data[j]+data[k]}')
                    print(f'{data[i]} * {data[j]} * {data[k]} = {data[i]*data[j]*data[k]}')
                    exit()

    
                