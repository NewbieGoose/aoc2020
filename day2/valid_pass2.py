#!/usr/bin/env python3

import sys

def policy_split(line):
    policy, password = line.split(':')
    crange, char     = policy.split()
    start, end = crange.split('-')
    return (password.strip(), char, (int(start), int(end)) )

def xor_positions(password, character, positions):
    pos1, pos2 = positions
    return (password[pos1-1] == character) ^ (password[pos2-1] == character)

if __name__ == "__main__":
    FILENAME = 'input.txt'
    if len(sys.argv) > 1:
        FILENAME = sys.argv[1]
    
    with open(FILENAME) as inp:
        data  = [ xor_positions(*policy_split(x.strip())) for x in inp.readlines()]
    print(data.count(True))
    