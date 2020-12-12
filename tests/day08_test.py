#!/usr/bin/env python3

import unittest
import os
import sys

import day08
from utils import read_inputfile

class DayTest(unittest.TestCase):

    def test_part1_on_example_data(self):
        input = read_inputfile("example08.txt")
        self.assertEqual(day08.part1(input), 5)

    def test_part2_on_example_data(self):
        input = read_inputfile("example08.txt")
        self.assertEqual(day08.part2(input), 8)

if __name__ == "__main__": 
    unittest.main()