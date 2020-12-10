#!/usr/bin/env python3

import re
import os
import sys

from typing import List
from typing import Tuple
from typing import Dict

# Convert input into list of ints
def read_numbers(input: List[str]) -> List[int]:
    result = [ int(line) for line in input ]
    return result

def find_differences_in_adapter_chain(adapters: List[int]) -> Tuple[int, int]:
    adapters.sort()
    i = 0
    prev = 0
    ones = 0
    threes = 0
    while i < len(adapters):
        next = adapters[i]
        if next - prev == 1:
            ones += 1
        else:
            if next -prev == 3:
                threes += 1
            else:
                raise ValueError("Difference != 0 or 3")
        prev = next
        i += 1
    threes += 1
    return (ones, threes)

def find_adapter_chains(current: int, pos: int, adapters: List[int], chain : List[int]) -> List[List[int]]:
    chains: List[List[int]] = []
    chain.append(current) 
    if pos == len(adapters):
        return [chain]
    while pos < len(adapters):
        next = adapters[pos]
        pos += 1
        difference = next - current
        if difference > 3:
            break
        if difference <= 3 :
            chains = chains + (find_adapter_chains(next, pos, adapters, chain.copy()))
        print(chains)
    return chains

def count_adapter_chains(start: int, adapters: List[int], memo: Dict[int, int]=None) -> int:
    if memo == None:
        memo = {}
    current = adapters[start]
    if start == len(adapters)-1:
        return 1
    if memo and start in memo:
        return memo[start]
    chains = 0
    pos = start + 1 
    while pos < len(adapters):
        next = adapters[pos]
        difference = next - current
        if difference > 3:
            break
        if difference <= 3 :
            chains = chains + (count_adapter_chains(pos, adapters, memo))
        pos += 1
    if memo:
        memo[start] = chains    
    return chains

def part1(input):
    adapters = read_numbers(input)
    (ones, threes) = find_differences_in_adapter_chain(adapters)
    result = ones * threes
    return result

def part2(input):
    adapters = read_numbers(input)
    adapters.append(0)
    device = max(adapters) + 3
    adapters.append(device)
    adapters.sort()
    print(adapters)
    chains = count_adapter_chains(0, adapters)
    return chains

def main():    

    # Official input
    input_file = os.path.abspath(os.path.dirname(__file__)) + os.path.sep + "input10.txt"
    with open(input_file) as f:
        input = [l.strip() for l in f]

    print("The solution for part 1 on the official input is %d" % (part1(input)))
    print("The solution for part 2 on the official input is %d" % (part2(input)))

if __name__ == "__main__": 
    main()

