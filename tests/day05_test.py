#!/usr/bin/env python3

import unittest
import os
import sys

import day05
from utils import read_inputfile
class Day05Test(unittest.TestCase):

    def test_bisect(self):
        self.assertEqual(day05.bisect(0, 127), 63)
        self.assertEqual(day05.bisect(0, 63), 31)
        self.assertEqual(day05.bisect(32, 63), 47)

    def test_compute_seat(self):
        self.assertEqual(day05.compute_seat("BFFFBBFRRR"), (70, 7))
        self.assertEqual(day05.compute_seat("FFFBBBFRRR"), (14, 7))
        self.assertEqual(day05.compute_seat("BBFFBBFRLL"), (102, 4))

    def test_compute_seat2(self):
        self.assertEqual(day05.compute_seat2("BFFFBBFRRR"), (70, 7))
        self.assertEqual(day05.compute_seat2("FFFBBBFRRR"), (14, 7))
        self.assertEqual(day05.compute_seat2("BBFFBBFRLL"), (102, 4))


    def test_part1(self):
        input = ["BFFFBBFRRR", "FFFBBBFRRR", "BBFFBBFRLL"]
        self.assertEqual(day05.part1(input), 820)

    def test_part1_on_example_data(self):
        input = read_inputfile("example05.txt")
        self.assertEqual(day05.part1(input), 820)

if __name__ == "__main__": 
    unittest.main()