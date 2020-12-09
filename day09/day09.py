#!/usr/bin/env python3

import re
import os
import sys

from typing import List

def read_numbers(input: List[str]) -> List[int]:
    result = [ int(line) for line in input ]
    return result


def verify_number(number: int, to_consider: List[int]) -> bool:
    # print("%d -> %s" % (number, to_consider))
    for first in to_consider:
        for second in to_consider:
            if first != second:
                if number == first + second:
                    # print("%d %d" % (first, second))
                    return True
    return False

def find_weakness(input: List[int], preamble: int) -> int:
    if len(input) <= preamble + 1:
        raise ValueError("Input to short")
    to_consider = input[:preamble]
    input = input[preamble:]
    while len(input) > 0:
        next = input[0]
        input = input[1:]
        if not verify_number(next, to_consider):
            return next
        to_consider.append(next)
        to_consider = to_consider[1:] 
    raise ValueError("No weakness found")

def find_contiguous_block(input: List[int], weakness: int) -> List[int]:
    result : List[int] = []
    i = 0
    sum = 0
    while i < len(input):
        sum = 0
        result = []
        j = i + 1
        while j < len(input):
            sum += input[j]
            result.append(input[j])
            if sum == weakness:
                return result
            if sum > weakness:
                break
            j += 1    
        i += 1
    return result


def part1(input, preamble=25):
    return find_weakness(read_numbers(input), preamble)

def part2(input, preamble=25):
    numbers = read_numbers(input)
    weakness = find_weakness(numbers, preamble)
    block = find_contiguous_block(numbers, weakness)
    first = min(block)
    second = max(block)
    result = first + second
    return result

def main():    

    # Official input
    input_file = os.path.abspath(os.path.dirname(__file__)) + os.path.sep + "input09.txt"
    with open(input_file) as f:
        input = [l.strip() for l in f]

    print("The solution for part 1 on the official input is %d" % (part1(input)))
    print("The solution for part 2 on the official input is %d" % (part2(input)))

if __name__ == "__main__": 
    main()

