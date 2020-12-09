#!/usr/bin/env python3

import unittest
import os
import sys

import day09

class Day09Test(unittest.TestCase):

    def test_part1_on_example_data(self):
        input_file = os.path.abspath(os.path.dirname(__file__)) + os.path.sep + "example09.txt"
        with open(input_file) as f:
            input = [l.strip() for l in f]
        numbers = day09.read_numbers(input)
        self.assertEqual(day09.find_weakness(numbers, 5), 127)

    def test_find_contiguous_block(self):
        input_file = os.path.abspath(os.path.dirname(__file__)) + os.path.sep + "example09.txt"
        with open(input_file) as f:
            input = [l.strip() for l in f]
        numbers = day09.read_numbers(input)
        self.assertEqual(day09.find_contiguous_block(numbers, 127), [15, 25, 47, 40])

    def test_part2_on_example_data(self):
        input_file = os.path.abspath(os.path.dirname(__file__)) + os.path.sep + "example09.txt"
        with open(input_file) as f:
            input = [l.strip() for l in f]
        self.assertEqual(day09.part2(input, 5), 62)
        

if __name__ == "__main__": 
    unittest.main()