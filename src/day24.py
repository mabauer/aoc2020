#!/usr/bin/env python3

import re
import os
import sys
from typing import Dict, List, Set, Tuple

from utils import read_inputfile

# We are using axial or "skewed" coordinates, see https://www.redblobgames.com/grids/hexagons/
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
    # print(s)
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
    # print("%d, %d" % (x, y))
    i = 0
    for (dx, dy) in path:
        (x, y) = (x + dx, y + dy)
        # print("%s: %d, %d" % (tokens[i], x, y))
        i += 1
    print()
    return (x, y)

def create_tiles(input):
    black_tiles : Set[Tuple[int, int]]
    black_tiles = set()
    for line in input:  
        (x, y) = compute_tile(line)
        if (x, y) in black_tiles:
            black_tiles.remove((x, y))
        else:
            black_tiles.add((x, y))
    return black_tiles

def part1(input):
    black_tiles = create_tiles(input)
    result = len(black_tiles)
    return result

# This is a slightly modified version of the "Game of Life" from day 17.
class LivingArt:

    def __init__(self, black_tiles: Set[Tuple[int, int]]):
        self.black_tiles = black_tiles
        self.x_min = min([ x for (x, _) in self.black_tiles ])
        self.x_max = max([ x for (x, _) in self.black_tiles ])
        self.y_min = min([ y for (_, y) in self.black_tiles ])
        self.y_max = max([ y for (_, y) in self.black_tiles ])

    
    # Compute a new generation according to the rules of part 1
    # Returns True, if thee new generation differs from the old one.
    def next_generation(self) -> bool:

        # Expand game area
        self.y_min -= 1
        self.y_max += 1
        self.x_min -= 1
        self.x_max += 1

        # Precalculate the number of black adjacent tiles
        number_of_adjacent_blacks : Dict[Tuple[int, int], int] = {}
        for y in range(self.y_min, self.y_max + 1):
            for x in range(self.x_min, self.x_max + 1):
                number_of_adjacent_blacks[(x, y)] = self.count_adjacent_blacks(x, y)

        # Compute next generation
        changed = False
        for y in range(self.y_min, self.y_max + 1):
            for x in range(self.x_min, self.x_max + 1):
                was_black = (x, y) in self.black_tiles
                c = number_of_adjacent_blacks[(x, y)]
                # print(c, end="")
                if was_black and (c == 0 or c > 2):
                    self.black_tiles.remove((x, y))
                    changed = True
                if not was_black and c==2:
                    self.black_tiles.add((x,y))
                    changed = True
        return changed

    # Count the number of ajdacent black tiles for tile at (x, y)
    def count_adjacent_blacks(self, x: int, y: int) -> int:
        result = 0
        for dir in dirs.values():
            (x1, y1) = dir
            if (x+x1, y+y1) in self.black_tiles:
                result += 1
        return result

    # Count the number of black tiles
    def count_black_tiles(self):
        return len(self.black_tiles)

    def print(self):
        for y in range(self.y_min, self.y_max + 1):
            for x in range(self.x_min, self.x_max + 1):
                print(self.get_cell(x, y), end="")
            print()


def part2(input, max_days = 100):
    black_tiles = create_tiles(input)
    art = LivingArt(black_tiles)
    days = 0
    is_stable = False
    while days < max_days:
        days += 1
        is_stable = not art.next_generation()
        print("Day %d: %d" % (days, art.count_black_tiles()))
        if is_stable:
            break
    if is_stable:
        print("Stable after %d days." % days)
    result = art.count_black_tiles()
    return result

def main():    

    # Official input
    input = read_inputfile("input24.txt")

    print("The solution for part 1 on the official input is %d" % (part1(input)))
    print("The solution for part 2 on the official input is %d" % (part2(input)))

if __name__ == "__main__": 
    main()

