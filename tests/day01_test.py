#!/usr/bin/env python3

import unittest

from day01 import find_two_entries_for_2020, find_three_entries_for_2020

class Day01Test(unittest.TestCase):

    def test_part1_on_example_data(self):
        input = [1721, 979, 366, 299, 675, 1456]
        result = find_two_entries_for_2020(input)
        self.assertEqual(result, (1721, 299))

    def test_part2_on_example_data(self):
        input = [1721, 979, 366, 299, 675, 1456]
        result = find_three_entries_for_2020(input)
        self.assertEqual(result, (979, 366, 675))
   

if __name__ == "__main__": 
    unittest.main()