#!/usr/bin/env python3

import unittest
import os
import sys

import day06
from utils import read_inputfile

class Day06Test(unittest.TestCase):

    def test_part1_on_example_data(self):
        input = read_inputfile("example06.txt")
        self.assertEqual(day06.part1(input), 11)

    def test_part2(self):
        input = read_inputfile("example06.txt")
        self.assertEqual(day06.part2(input), 6)

if __name__ == "__main__": 
    unittest.main()