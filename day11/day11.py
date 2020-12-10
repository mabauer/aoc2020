#!/usr/bin/env python3

import re
import os
import sys

def part1(input):
    result = 0
    return result

def part2(input):
    result = 0
    return result

def main():    

    # Official input
    input_file = os.path.abspath(os.path.dirname(__file__)) + os.path.sep + "input11.txt"
    with open(input_file) as f:
        input = [l.strip() for l in f]

    print("The solution for part 1 on the official input is %d" % (part1(input)))
    print("The solution for part 2 on the official input is %d" % (part2(input)))

if __name__ == "__main__": 
    main()

