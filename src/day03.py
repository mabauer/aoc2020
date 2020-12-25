#!/usr/bin/env python3

import os
from functools import reduce

from utils import read_inputfile

# Count trees encountered in the map when applying a trajectory with parameters right, down 
def count_trees(map, right, down):
    count = 0
    x = 0
    y = 0
    while y < len(map):
        line = map[y]
        length = len (line)
        offset = x % length
        square = line[offset]
        if square == "#":
            count = count + 1
        x = x + right
        y = y + down
 
    return count

# Apply different strategies and multiply the results
def part2(map, strategies):
    results = [ count_trees(map, right, down) for (right, down) in strategies]
    multiply = lambda x, y: x * y
    result = reduce(multiply, results)
    return result

def main():

    input = read_inputfile("input03.txt")

    print("The trajectory encounters %d trees" % count_trees(input, 3, 1))

    # Predefined trajectory strategies for part two
    trajectory_strategies = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

    print("The solution for part is %d" % part2(input, trajectory_strategies))

if __name__ == "__main__": 
    main()

