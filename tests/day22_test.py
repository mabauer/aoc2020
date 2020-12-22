#!/usr/bin/env python3

import unittest

from day22 import part1, part2
from utils import read_inputfile

class Day22Test(unittest.TestCase):

    def test_part1_on_example_data(self):
        input = read_inputfile("example22.txt")
        self.assertEqual(part1(input), 306)

    def test_part2(self):
        input = [""]
        self.assertEqual(part2(input), 0)

if __name__ == "__main__": 
    unittest.main()