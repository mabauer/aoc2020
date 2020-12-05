#!/usr/bin/env python3

import unittest
import os
import sys

import day05

class Day05Test(unittest.TestCase):

    def test_compute05(self):
        input = [""]
        self.assertEqual(day05.compute05(input), 0)

    def test_compute05_on_example_data(self):
        input_file = os.path.abspath(os.path.dirname(__file__)) + os.path.sep + "example05.txt"
        with open(input_file) as f:
            input = [x.strip() for x in f]
        self.assertEqual(day05.compute05(input), 0)

if __name__ == "__main__": 
    unittest.main()