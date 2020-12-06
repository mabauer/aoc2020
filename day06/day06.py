#!/usr/bin/env python3

import re
import os
import sys

def compute06(input):
    result = 0
    return result

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

