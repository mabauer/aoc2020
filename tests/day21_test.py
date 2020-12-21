#!/usr/bin/env python3

import unittest

from day21 import part1, part2
from utils import read_inputfile

class Day21Test(unittest.TestCase):

    def test_part1_on_example_data(self):
        input = read_inputfile("example21.txt")
        self.assertEqual(part1(input), 5)

    def test_part2(self):
        input = [""]
        self.assertEqual(part2(input), 0)

if __name__ == "__main__": 
    unittest.main()