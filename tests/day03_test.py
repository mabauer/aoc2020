#!/usr/bin/env python3

import unittest

from day03 import count_trees, part2

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

class Day03Test(unittest.TestCase):

    def test_part1_on_example_data(self):
        self.assertEqual(count_trees(input1, 3, 1), 7)

    def test_part2_different_strategies(self):
        self.assertEqual(count_trees(input1, 1, 1), 2)
        self.assertEqual(count_trees(input1, 5, 1), 3)
        self.assertEqual(count_trees(input1, 7, 1), 4)
        self.assertEqual(count_trees(input1, 1, 2), 2)

    def test_part2_on_example_data(self):
        # Predefined trajectory strategies for part two
        trajectory_strategies = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
        self.assertEqual(part2(input1, trajectory_strategies), 336)
   

if __name__ == "__main__": 
    unittest.main()