#!/usr/bin/env python3

import unittest
import os
import sys

from day18 import Expression, part1, part2
from utils import read_inputfile

class Day18Test(unittest.TestCase):

    def test_tokenize(self):
        expr = Expression("1 + (3*4)")
        self.assertEqual(expr.tokens, ["1", "+", "(", "3", "*", "4", ")"])

    def test_expressions(self):
        self.assertEqual(Expression("1").eval(), 1)
        self.assertEqual(Expression("1 + 3").eval(), 4)
        self.assertEqual(Expression("1 * 3").eval(), 3)
        # self.assertEqual(Expression("1 + 2 * 3").eval(), 9)
        self.assertEqual(Expression("(1 * 3)").eval(), 3)
        self.assertEqual(Expression("1 + (3*4)").eval(), 13)
        self.assertEqual(Expression("(3+4) * 2").eval(), 14)
        

    def test_example_expressions(self):
        self.assertEqual(Expression("2 * 3 + (4 * 5)").eval(), 26)
        self.assertEqual(Expression("5 + (8 * 3 + 9 + 3 * 4 * 3)").eval(), 437)
        self.assertEqual(Expression("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))").eval(), 12240)
        self.assertEqual(Expression("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2").eval(), 13632)

    def test_part2(self):
        input = [""]
        self.assertEqual(part2(input), 0)

if __name__ == "__main__": 
    unittest.main()