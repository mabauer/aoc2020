#!/usr/bin/env python3

import unittest
import os
import sys

import day09
from utils import read_inputfile

examplefile = "example09.txt"

class Day09Test(unittest.TestCase):

    def test_part1_on_example_data(self):
        input = read_inputfile(examplefile)
        numbers = day09.read_numbers(input)
        self.assertEqual(day09.find_weakness(numbers, 5), 127)

    def test_find_contiguous_block(self):
        input = read_inputfile(examplefile)
        numbers = day09.read_numbers(input)
        self.assertEqual(day09.find_contiguous_block(numbers, 127), [15, 25, 47, 40])

    def test_part2_on_example_data(self):
        input = read_inputfile(examplefile)
        self.assertEqual(day09.part2(input, 5), 62)
        

if __name__ == "__main__": 
    unittest.main()