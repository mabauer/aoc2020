#!/usr/bin/env python3

import unittest
import os
import sys

import day11

class Day11Test(unittest.TestCase):

    def test_part1_on_example_data(self):
        input_file = os.path.abspath(os.path.dirname(__file__)) + os.path.sep + "example11.txt"
        with open(input_file) as f:
            input = [l.strip() for l in f]
        self.assertEqual(day11.part1(input), 0)

    def test_part2(self):
        input = [""]
        self.assertEqual(day11.part2(input), 0)

if __name__ == "__main__": 
    unittest.main()