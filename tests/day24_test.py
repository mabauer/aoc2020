#!/usr/bin/env python3

import unittest
import os
import sys

from day24 import compute_tile, part1, part2
from utils import read_inputfile

class Day24Test(unittest.TestCase):

    def test_compute_tile(self):
        self.assertEqual(compute_tile("esew"), (1, -1))
        self.assertEqual(compute_tile("ew"), (0, 0))
        self.assertEqual(compute_tile("nesw"), (0, 0))
        self.assertEqual(compute_tile("nwswe"), (0, 0))
        self.assertEqual(compute_tile("nwwswee"), (0, 0))

    def test_part1_on_example_data(self):
        input = read_inputfile("example24.txt")
        self.assertEqual(part1(input), 10)

    def test_part2(self):
        input = [""]
        self.assertEqual(part2(input), 0)

if __name__ == "__main__": 
    unittest.main()