#!/usr/bin/env python3

import re
import os
import sys

def parse_groups(input):
    groups = []
    answers = {}
    for line in input:
        if line == "":
            groups.append(answers)
            answers = {}
        i = 0
        while i < len(line):
            if line[i] >= 'a' and line[i] <='z':
                if line[i] in answers:
                    answers[line[i]] =  answers[line[i]] + 1
                else:
                    answers[line[i]] = 1
            i = i + 1
    if line != "":
        groups.append(answers)
    return groups 


def compute06(input):
    groups = parse_groups(input)
    # print(groups)
    sum = 0
    for group in groups:
        sum = sum + len(group)
    return sum

def compute06b(input):
    result = 0
    return result

def main():    

    # Official input
    input_file = os.path.abspath(os.path.dirname(__file__)) + os.path.sep + "input06.txt"
    with open(input_file) as f:
        input = [x.strip() for x in f]

    print("The solution for part 1 on the official input is %d" % (compute06(input)))
    print("The solution for part 2 on the official input is %d" % (compute06b(input)))

if __name__ == "__main__": 
    main()

