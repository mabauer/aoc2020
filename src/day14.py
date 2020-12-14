#!/usr/bin/env python3

import re

from typing import Dict, List

from utils import read_inputfile

def to_binary_str(value : int):
    result = "{:036b}".format(value)
    return result

def bitwise_not(n, numbits=36):
    return (1 << numbits) - 1 - n

def apply_mask(value: int, mask: str):
    m1 = int(mask.replace("X", "0"), 2)
    m2 = int(mask.replace("X", "1"), 2)
    value = value | m1
    value = value & m2
    # print("Masked value: %s" % to_binary_str(value))
    return value

def apply_mask_and_floating_bits(value: int, mask: str) -> List[int]:
    m1 = int(mask.replace("X", "0"), 2)
    value = value | m1
    result : List[int]= []
    result.append(value)
    for i in range(0, len(mask)):
        if mask[len(mask)-1-i] == "X":
            old_result = result.copy()
            result = []
            for addr in old_result:
                result.append(addr & ~(1 << i)) # Append with ith bit = 0
                result.append(addr | (1 << i))  # Append with ith bit = 1
            # print(result)
    return result

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

def run_instructions_part2(input):
    mask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    mem : Dict[int, int] = {}
    for line in input:
        s = line.replace(" ", "")
        (lhs, rhs) = s.split("=")
        if lhs == "mask":
            mask = rhs
        else:
            mo = re.search("mem\[([0-9]+)\]", lhs)
            original_addr = int(mo.group(1))
            addresses = apply_mask_and_floating_bits(original_addr, mask)
            value = int(rhs)
            for addr in addresses:
                mem[addr] = value
    result = sum(mem.values())
    return result
        
def part1(input):
    result = run_instructions_part1(input)
    return result

def part2(input):
    result = run_instructions_part2(input)
    return result

def main():    

    # Official input
    input = read_inputfile("input14.txt")

    print("The solution for part 1 on the official input is %d" % (part1(input)))
    print("The solution for part 2 on the official input is %d" % (part2(input)))

if __name__ == "__main__": 
    main()

