#!/usr/bin/env python3

import os
from functools import reduce

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
def part_two(map, strategies):
    results = [ count_trees(map, right, down) for (right, down) in strategies]
    multiply = lambda x, y: x * y
    result = reduce(multiply, results)
    return result

def main():
    # Example
    input1 = [
        "..##.......", 
        "#...#...#..", 
        ".#....#..#.", 
        "..#.#...#.#", 
        ".#...##..#.", 
        "..#.##.....", 
        ".#.#.#....#", 
        ".#........#", 
        "#.##...#...", 
        "#...##....#", 
        ".#..#...#.#"]

    # Official input
    input_file = os.path.abspath(os.path.dirname(__file__)) + os.path.sep + "input03.txt"
    with open(input_file) as f:
        input2 = [x.strip() for x in f]

    print("The trajectory for the example data encounters %d trees" % (count_trees(input1, 3, 1)))
    print("The trajectory for the official input encounters %d trees" % (count_trees(input2, 3, 1)))

    # Predefined trajectory strategies for part two
    trajectory_strategies = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

    print("The solution for part two on the example data is %d" % (part_two(input1, trajectory_strategies)))
    print("The solution for part two on the official data is %d" % (part_two(input2, trajectory_strategies)))

if __name__ == "__main__": 
    main()

