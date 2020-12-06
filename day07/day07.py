#!/usr/bin/env python3

import re
import os
import sys

def compute07(input):
    result = 0
    return result

def compute07b(input):
    result = 0
    return result

def main():    

    # Official input
    input_file = os.path.abspath(os.path.dirname(__file__)) + os.path.sep + "input07.txt"
    with open(input_file) as f:
        input = [x.strip() for x in f]

    print("The solution for part 1 on the official input is %d" % (compute07(input)))
    print("The solution for part 2 on the official input is %d" % (compute07b(input)))

if __name__ == "__main__": 
    main()

