#!/usr/bin/env python3

import sys
    

if __name__ == "__main__":
    FILENAME = 'input.txt'
    if len(sys.argv) > 1:
        FILENAME = sys.argv[1]
    

    with open(FILENAME) as inp:
        jolts = [int(line) for line in inp.readlines()]

    jolts = sorted(jolts)
    jolts.insert(0,0)
    jolts.append(jolts[-1] + 3)
    print(jolts)

    dynamic = [0] * len(jolts)
    dynamic[0] = 1
    for index in range(len(dynamic)):
        for i in range(1,4):
            if index + i < len(dynamic) and jolts[index+i] - jolts[index] < 4:
                dynamic[index+i] += dynamic[index]
    print(f'Found {dynamic[-1]} arrangements')
