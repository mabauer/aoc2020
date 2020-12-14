#!/usr/bin/env python3

import re
import os
import sys
import math
from typing import Dict

from utils import read_inputfile

def to_binary_str(value : int):
    result = "{:036b}".format(value)
    return result

def bitwise_not(n, numbits=36):
    return (1 << numbits) - 1 - n

def apply_mask(value: int, mask: str):
    m1 = int(mask.replace("X", "0"), 2)
    m2 = int(mask.replace("X", "1"), 2)
    # print("value: %s" % to_binary_str(value))
    # print("mask: %s" % mask)
    value = value | m1
    # print("after m1: %s" % to_binary_str(value))
    value = value & m2
    # print("after m2: %s" % to_binary_str(value))
    return value

def run_instructions_part1(input):
    mask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    mem : Dict[int, int] = {}
    for line in input:
        s = line.replace(" ", "")
        (lhs, rhs) = s.split("=")
        if lhs == "mask":
            mask = rhs
        else:
            mo = re.search("mem\[([0-9]+)\]", lhs)
            addr = int(mo.group(1))
            value = int(rhs)
            mem[addr] = apply_mask(value, mask)
    result = sum(mem.values())
    return result
        
def part1(input):
    result = run_instructions_part1(input)
    return result

def part2(input):
    result = 0
    return result

def main():    

    # Official input
    input = read_inputfile("input14.txt")

    print("The solution for part 1 on the official input is %d" % (part1(input)))
    print("The solution for part 2 on the official input is %d" % (part2(input)))

if __name__ == "__main__": 
    main()

