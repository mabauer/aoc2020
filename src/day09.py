#!/usr/bin/env python3

import re
import os
import sys

from typing import List

from utils import read_inputfile

# Convert input into list of ints
def read_numbers(input: List[str]) -> List[int]:
    result = [ int(line) for line in input ]
    return result

# Verify if number equals to the sum of some pair in to_consider
def verify_number(number: int, to_consider: List[int]) -> bool:
    # print("%d -> %s" % (number, to_consider))
    for first in to_consider:
        for second in to_consider:
            if first != second:
                if number == first + second:
                    # print("%d %d" % (first, second))
                    return True
    return False

# Find the weakness in a list of ints, i.e. a number that cannot be reproduced by the sum of 
# some pair of numbers in a rolling window of numbers previously read
# Consider a sliding/rolling window of window_size.
def find_weakness(input: List[int], window_size: int) -> int:
    if len(input) <= window_size + 1:
        raise ValueError("Input too short")
    # Prefill window
    sliding_window = input[:window_size]
    input = input[window_size:]
    while len(input) > 0:
        # "Pop" the next item from the input 
        next = input[0]
        input = input[1:]
        if not verify_number(next, sliding_window):
            return next
        # Move sliding window by 1
        sliding_window.append(next)
        sliding_window = sliding_window[1:] 
    raise ValueError("No weakness found")

# Find a contiguous block of numbers whose sum equals weakness
def find_contiguous_block(input: List[int], weakness: int) -> List[int]:
    block : List[int] = []
    i = 0
    sum = 0
    while i < len(input):
        j = i 
        # Try building a block starting from position j
        sum = 0
        block = []
        while j < len(input) and sum < weakness:
            next = input[j]
            sum += next
            block.append(next)
            if sum == weakness:
                return block
            j += 1    
        i += 1
    return block


def part1(input, window_size=25):
    return find_weakness(read_numbers(input), window_size)

def part2(input, window_size=25):
    numbers = read_numbers(input)
    weakness = find_weakness(numbers, window_size)
    block = find_contiguous_block(numbers, weakness)
    first = min(block)
    second = max(block)
    result = first + second
    return result

def main():    

    # Official input
    input = read_inputfile("input09.txt")

    print("The solution for part 1 on the official input is %d" % (part1(input)))
    print("The solution for part 2 on the official input is %d" % (part2(input)))

if __name__ == "__main__": 
    main()

