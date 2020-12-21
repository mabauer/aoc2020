#!/usr/bin/env python3

import unittest

from day21 import part1, part2, solve
from utils import read_inputfile

class Day21Test(unittest.TestCase):

    def test_part1_on_example_data(self):
        input = read_inputfile("example21.txt")
        self.assertEqual(part1(input), 5)

    def test_solve(self):
        problem = {
            'cqvc': {'wheat'},
            'nhx': {'fish'},
            'rrjb': {'sesame'},
            'xmhsbd': {'wheat', 'peanuts', 'fish'},
            'ntft': {'eggs', 'sesame', 'fish'},
            'xzhxj': {'wheat', 'eggs', 'shellfish'},
            'kfxr': {'eggs', 'peanuts', 'nuts', 'soy'},
            'chbtp': {'sesame', 'shellfish', 'fish', 'soy'}
        }
        solution = solve(problem)
        print(solution)

    def test_part2(self):
        input = read_inputfile("example21.txt")
        self.assertEqual(part2(input), "mxmxvkd,sqjhc,fvjkl")

if __name__ == "__main__": 
    unittest.main()