#!/usr/bin/env python3

import re
import os
import sys
from typing import Set, Tuple

from utils import read_inputfile

dirs = {
    "e" : ( 1,  0),
    "w" : (-1,  0),
    "ne": ( 0,  1),
    "nw": (-1,  1),
    "se": ( 1, -1),
    "sw": ( 0, -1)   
}

def compute_tile(s : str) -> Tuple[int, int]:
    i = 0
    dir = ""
    path = []
    tokens = []
    print(s)
    while i < len(s):
        c = s[i]
        if c in ["e", "w"]:
            dir = dir + c
            tokens.append(dir)
            path.append(dirs[dir])
            dir = ""
        if c in ["n", "s"]:
            dir = c
        i += 1
    (x, y) = (0, 0)
    print("%d, %d" % (x, y))
    i = 0
    for (dx, dy) in path:
        (x, y) = (x + dx, y + dy)
        print("%s: %d, %d" % (tokens[i], x, y))
        i += 1
    print()
    return (x, y)

def part1(input):
    black_tiles : Set[Tuple[int, int]]
    black_tiles = set()
    for line in input:  
        (x, y) = compute_tile(line)
        if (x, y) in black_tiles:
            black_tiles.remove((x, y))
        else:
            black_tiles.add((x, y))
    result = len(black_tiles)
    return result

def part2(input):
    result = 0
    return result

def main():    

    # Official input
    input = read_inputfile("input24.txt")

    print("The solution for part 1 on the official input is %d" % (part1(input)))
    print("The solution for part 2 on the official input is %d" % (part2(input)))

if __name__ == "__main__": 
    main()

