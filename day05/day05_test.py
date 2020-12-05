#!/usr/bin/env python3

import unittest
import os
import sys

import day05
class Day05Test(unittest.TestCase):

    def test_bisect(self):
        self.assertEqual(day05.bisect(0, 127), 63)
        self.assertEqual(day05.bisect(0, 63), 31)
        self.assertEqual(day05.bisect(32, 63), 47)


    def test_compute_seat(self):
        self.assertEqual(day05.compute_seat("BFFFBBFRRR"), (70, 7))
        self.assertEqual(day05.compute_seat("FFFBBBFRRR"), (14, 7))
        self.assertEqual(day05.compute_seat("BBFFBBFRLL"), (102, 4))

    def test_compute05(self):
        input = ["BFFFBBFRRR", "FFFBBBFRRR", "BBFFBBFRLL"]
        self.assertEqual(day05.compute05(input), 820)

    def test_compute05_on_example_data(self):
        input_file = os.path.abspath(os.path.dirname(__file__)) + os.path.sep + "example05.txt"
        with open(input_file) as f:
            input = [x.strip() for x in f]
        self.assertEqual(day05.compute05(input), 820)

if __name__ == "__main__": 
    unittest.main()