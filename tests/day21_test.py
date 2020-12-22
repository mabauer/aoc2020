#!/usr/bin/env python3

import unittest

from day21 import part1, part2, find_matching
from utils import read_inputfile

class Day21Test(unittest.TestCase):

    def test_part1_on_example_data(self):
        input = read_inputfile("example21.txt")
        self.assertEqual(part1(input), 5)

    def test_find_matching(self):
        candidates = {
            'cqvc': {'wheat'},
            'nhx': {'fish'},
            'rrjb': {'sesame'},
            'xmhsbd': {'wheat', 'peanuts', 'fish'},
            'ntft': {'eggs', 'sesame', 'fish'},
            'xzhxj': {'wheat', 'eggs', 'shellfish'},
            'kfxr': {'eggs', 'peanuts', 'nuts', 'soy'},
            'chbtp': {'sesame', 'shellfish', 'fish', 'soy'}
        }
        solution = find_matching(candidates)
        self.assertIsNotNone(solution)
        # print(solution)
        self.assertEqual(solution, {
            'cqvc': 'wheat', 
            'nhx': 'fish', 
            'rrjb': 'sesame', 
            'xmhsbd': 'peanuts', 
            'ntft': 'eggs', 
            'xzhxj': 'shellfish', 
            'kfxr': 'nuts', 
            'chbtp': 'soy'})
        impossible = {
            'cqvc': {'wheat'},
            'nhx': {'fish'},
            'rrjb': {'sesame'},
            'xmhsbd': {'wheat', 'peanuts', 'fish'},
            'ntft': {'eggs', 'sesame', 'fish'},
            'xzhxj': {'wheat', 'eggs', 'shellfish'},
            'kfxr': {'eggs', 'peanuts', 'nuts', 'soy'},
            'chbtp': {'sesame', 'shellfish', 'fish'}  # soy is missing here!
        }
        self.assertIsNone(find_matching(impossible))

    def test_part2(self):
        input = read_inputfile("example21.txt")
        self.assertEqual(part2(input), "mxmxvkd,sqjhc,fvjkl")

if __name__ == "__main__": 
    unittest.main()