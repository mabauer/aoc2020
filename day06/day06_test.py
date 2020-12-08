#!/usr/bin/env python3

import unittest
import os
import sys

import day06

class Day06Test(unittest.TestCase):

    def test_part1_on_example_data(self):
        input_file = os.path.abspath(os.path.dirname(__file__)) + os.path.sep + "example06.txt"
        with open(input_file) as f:
            input = [x.strip() for x in f]
        self.assertEqual(day06.part1(input), 11)

    def test_part2(self):
        input_file = os.path.abspath(os.path.dirname(__file__)) + os.path.sep + "example06.txt"
        with open(input_file) as f:
            input = [x.strip() for x in f]
        self.assertEqual(day06.part2(input), 6)

if __name__ == "__main__": 
    unittest.main()