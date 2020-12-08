#!/usr/bin/env python3

import unittest
import os
import sys

import day08

class DayTest(unittest.TestCase):

    def test_part1_on_example_data(self):
        input_file = os.path.abspath(os.path.dirname(__file__)) + os.path.sep + "example08.txt"
        with open(input_file) as f:
            input = [l.strip() for l in f]
        self.assertEqual(day08.part1(input), 5)

    def test_part2_on_example_data(self):
        input_file = os.path.abspath(os.path.dirname(__file__)) + os.path.sep + "example08.txt"
        with open(input_file) as f:
            input = [l.strip() for l in f]
        self.assertEqual(day08.part2(input), 8)

if __name__ == "__main__": 
    unittest.main()