#!/usr/bin/env python3

import sys
    

if __name__ == "__main__":
    FILENAME = 'input.txt'
    if len(sys.argv) > 1:
        FILENAME = sys.argv[1]
    

    with open(FILENAME) as inp:
        jolts = [int(line) for line in inp.readlines()]

    jolts = sorted(jolts)
    differences = [0,0,0]

    curr_jolt = 0
    for j in jolts:
        diff = j - curr_jolt
        differences[diff - 1] += 1
        curr_jolt = j
    differences[2] += 1
    print(differences)
    print(differences[0]*differences[2])