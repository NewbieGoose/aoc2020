#!/usr/bin/env python3

import sys

questions = "abcxyz"

if __name__ == "__main__":
    FILENAME = 'input.txt'
    if len(sys.argv) > 1:
        FILENAME = sys.argv[1]

    group_answers = 0
    
    with open(FILENAME) as fd:
        group_answer = set()
        for line in fd:
            line  = line.strip()
            if line:
                for answer in line:
                    group_answer.add(answer)
            else:
                group_answers += len(group_answer)
                group_answer = set()
        if group_answer:
            group_answers += len(group_answer)
        print(group_answers)