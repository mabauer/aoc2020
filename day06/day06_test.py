#!/usr/bin/env python3

import unittest
import os
import sys

import day06

class Day06Test(unittest.TestCase):

    def test_compute06_on_example_data(self):
        input_file = os.path.abspath(os.path.dirname(__file__)) + os.path.sep + "example06.txt"
        with open(input_file) as f:
            input = [x.strip() for x in f]
        self.assertEqual(day06.compute06(input), 11)

    def test_compute06b(self):
        input = [""]
        self.assertEqual(day06.compute06b(input), 0)

if __name__ == "__main__": 
    unittest.main()