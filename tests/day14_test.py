#!/usr/bin/env python3

import unittest
import os
import sys

from day14 import apply_mask, part1, part2, to_binary_str
from utils import read_inputfile

class Day14Test(unittest.TestCase):

    def test_to_binary_str(self):
        self.assertEqual(to_binary_str(101), "000000000000000000000000000001100101")

    def test_apply_mask(self):
        mask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X"
        self.assertEqual(apply_mask(11, mask), 73)

    def test_part1_on_example_data(self):
        input = read_inputfile("example14.txt")
        self.assertEqual(part1(input), 165)

    def test_part2(self):
        input = [""]
        self.assertEqual(part2(input), 0)

if __name__ == "__main__": 
    unittest.main()