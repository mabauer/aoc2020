#!/usr/bin/env python3

import re
import os
import sys

def compute05(input):
    result = 0
    return result

def main():    

    # Official input
    input_file = os.path.abspath(os.path.dirname(__file__)) + os.path.sep + "input05.txt"
    with open(input_file) as f:
        input = [x.strip() for x in f]

    print("The solution for part 1 on the official input is %d" % (compute05(input)))
    print("The solution for part 2 on the official input is %d" % (compute05(input)))

if __name__ == "__main__": 
    main()

