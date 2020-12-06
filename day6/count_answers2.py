#!/usr/bin/env python3

import sys

questions = "abcxyz"

if __name__ == "__main__":
    FILENAME = 'input.txt'
    if len(sys.argv) > 1:
        FILENAME = sys.argv[1]

    group_answers = 0
    
    with open(FILENAME) as fd:
        group_answer = None
        for line in fd:
            line  = line.strip()
            if line:
                single_answer = set(line)
                if group_answer is None:
                    group_answer = single_answer
                group_answer = group_answer.intersection(single_answer)
            else:
                group_answers += len(group_answer)
                group_answer = None
        if group_answer:
            group_answers += len(group_answer)
        print(group_answers)