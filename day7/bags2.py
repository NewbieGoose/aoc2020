#! /usr/bin/env python3

import re
import sys

def parse_bags(line):
    def good_split(x):
        x = x.split(' ',1)
        return (x[1], int(x[0]))
    pattern = r'((?:\d+ )?\w+ \w+) bags?'
    result = re.findall(pattern,line)
    key, values = result[0], [good_split(x) for x in result[1:] if x != "no other"]
    return key, tuple(values)

if __name__ == "__main__":
    my_bag = 'shiny gold'
    FILENAME = 'input.txt'
    if len(sys.argv) > 1:
        FILENAME = sys.argv[1]

    with open(FILENAME) as inp:
        bags = dict(parse_bags(line.strip()) for line in inp.readlines())

    stack = [(my_bag,1)]
    s = 0
    while stack:
        bag, num = stack.pop()
        s += num
        neighbors = bags.get(bag, [])
        for neighbor, n in neighbors:
            stack.append((neighbor,n*num))

        
    print(s - 1)