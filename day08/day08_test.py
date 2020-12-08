#!/usr/bin/env python3

import unittest
import os
import sys

import day08

class DayTest(unittest.TestCase):

    def test_compute_on_example_data(self):
        input_file = os.path.abspath(os.path.dirname(__file__)) + os.path.sep + "example08.txt"
        with open(input_file) as f:
            input = [x.strip() for x in f]
        self.assertEqual(day08.compute08(input), 5)

    def test_computeb(self):
        input = [""]
        self.assertEqual(day08.compute08b(input), 0)

if __name__ == "__main__": 
    unittest.main()