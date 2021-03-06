#!/usr/bin/env python3

import re
import os
import sys

from typing import List
from typing import Tuple
from typing import Dict

from utils import read_inputfile

# Convert input into list of ints
def read_numbers(input: List[str]) -> List[int]:
    result = [ int(line) for line in input ]
    return result

# Count the 1- and 3-step joltage jumps for part 1
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

# Compute all possible varinats of adapter chains
# This does not terminate for longer inputs!!!
def find_adapter_chains(start: int, adapters: List[int], chain=None) -> List[List[int]]:
    if chain == None:
        chain = []
    current = adapters[start]
    chain.append(current)
    # print("%s, -- %d" % (chain, current))
    if start == len(adapters)-1:
        return [chain]
    chains: List[List[int]] = []
    pos = start + 1 
    while pos < len(adapters):
        next = adapters[pos]
        difference = next - current
        if difference > 3:
            break
        if difference <= 3 :
            chains = chains + find_adapter_chains(pos, adapters, chain.copy())
        pos += 1
    return chains

# Count the number of all possible varinats of adapter chains using dynamic programming
# By memorizing previously computed partial results this implementation works for larger inputs!
def count_adapter_chains(start: int, adapters: List[int], memo: Dict[int, int]=None) -> int:
    if memo == None:
        memo = {}
    current = adapters[start]
    if start == len(adapters)-1:
        return 1
    if memo is not None and start in memo:
        return memo[start]
    chains = 0
    pos = start + 1 
    while pos < len(adapters):
        next = adapters[pos]
        difference = next - current
        if difference > 3:
            break
        if difference <= 3 :
            chains = chains + count_adapter_chains(pos, adapters, memo)
        pos += 1
    if memo is not None:
        memo[start] = chains    
    return chains

def count_adapter_chains_iterative(adapters: List[int]) -> int:
    # maybe_skipped[i] will contain a list of all adapters that can possibly omitted 
    # while building an adapter chain starting from adapter with joltage i
    maybe_skipped : Dict[int, List[int]] = {}
    for adapter in adapters:
        maybe_skipped[adapter] = []
    for adapter in adapters:
        for difference in [1, 2, 3]:
            next = adapter + difference
            if next in adapters:
                maybe_skipped[adapter].append(next)

    # Count the number of possible chains backwards: 
    # For the last adapter, there is only one possibility of building a chain
    # For earlier ones, it is the sum of all possibilities of those that we have previously computed.
    # For [0, 1, 3, 4]:
    # skippable[0] = [1, 3], skippable[1] = [3, 4], skippable[3] = [4], skippable[4]=[]
    # chains[4] = 1, 
    # chains[3] = chains[4] = 1
    # chains[1] = chains[3] + chains[4] = 1 + 1 = 2
    # chains[0] = chains[1] + chains[3] = 2 + 1 = 3 <= There are 3 possible chains
    chains : Dict[int, int] = {}
    chains[adapters[len(adapters)-1]] = 1
    for adapter in reversed(adapters[0:len(adapters)-1]):
        sum = 0
        # print("%d: %s" % (adapter, maybe_skipped[adapter]))
        for next in maybe_skipped[adapter]:
            sum += chains[next]
        chains[adapter] = sum
    return chains[0]
            
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
    # chains = count_adapter_chains(0, adapters, {})
    chains = count_adapter_chains_iterative(adapters)
    return chains

def main():    

    # Official input
    input = read_inputfile("input10.txt")

    print("The solution for part 1 on the official input is %d" % (part1(input)))
    print("The solution for part 2 on the official input is %d" % (part2(input)))

if __name__ == "__main__": 
    main()

