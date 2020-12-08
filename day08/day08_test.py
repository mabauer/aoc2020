#!/usr/bin/env python3

import unittest
import os
import sys

import day08

class DayTest(unittest.TestCase):

    def test_compute08_on_example_data(self):
        input_file = os.path.abspath(os.path.dirname(__file__)) + os.path.sep + "example08.txt"
        with open(input_file) as f:
            input = [l.strip() for l in f]
        self.assertEqual(day08.compute08(input), 5)

    def test_compute08b_on_example_data(self):
        input_file = os.path.abspath(os.path.dirname(__file__)) + os.path.sep + "example08.txt"
        with open(input_file) as f:
            input = [l.strip() for l in f]
        self.assertEqual(day08.compute08b(input), 8)

if __name__ == "__main__": 
    unittest.main()