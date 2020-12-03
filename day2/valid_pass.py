#!/usr/bin/env python3

import sys

def policy_split(line):
    policy, password = line.split(':')
    crange, char     = policy.split()
    start, end = crange.split('-')
    return (password, char, (int(start), int(end)) )

def count_range(password, character, crange):
    start, end = crange
    for letter in password:
        if letter == character:
            end -= 1
            start -= 1
            if end < 0:
                return False
    return start <= 0

if __name__ == "__main__":
    FILENAME = 'input.txt'
    if len(sys.argv) > 1:
        FILENAME = sys.argv[1]
    
    with open(FILENAME) as inp:
        data  = [ count_range(*policy_split(x.strip())) for x in inp.readlines()]
    print(data.count(True))
    