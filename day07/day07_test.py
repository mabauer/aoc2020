#!/usr/bin/env python3

import unittest
import os
import sys

import day07

class Day07Test(unittest.TestCase):

    def test_compute07_on_example_data(self):
        input_file = os.path.abspath(os.path.dirname(__file__)) + os.path.sep + "example07.txt"
        with open(input_file) as f:
            input = [x.strip() for x in f]
        self.assertEqual(day07.compute07(input), 0)

    def test_compute07b(self):
        input = [""]
        self.assertEqual(day07.compute07b(input), 0)

if __name__ == "__main__": 
    unittest.main()