#!/usr/bin/env python3

import unittest
import os
import sys

import day10

class Day10Test(unittest.TestCase):

    def test_part1_on_example_data(self):
        input_file = os.path.abspath(os.path.dirname(__file__)) + os.path.sep + "example10.txt"
        with open(input_file) as f:
            input = [l.strip() for l in f]
        self.assertEqual(day10.part1(input), 0)

    def test_part2(self):
        input = [""]
        self.assertEqual(day10.part2(input), 0)

if __name__ == "__main__": 
    unittest.main()