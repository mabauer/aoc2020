#!/usr/bin/env python3

import unittest

from day18 import Expression, Expression2, part1, part2
from utils import read_inputfile

class Day18Test(unittest.TestCase):

    def test_tokenize(self):
        expr = Expression("1 + (3*4)")
        self.assertEqual(expr.tokens, ["1", "+", "(", "3", "*", "4", ")"])
        # "2/" throw a syntax error
        with self.assertRaises(ValueError):
            Expression("2/")

    def test_parsing_errors(self):
        # "2+3(" should throw a syntax error
        with self.assertRaises(ValueError):
            Expression("2+3(").eval()

    def test_expressions(self):
        self.assertEqual(Expression("1").eval(), 1)
        self.assertEqual(Expression("1 + 3").eval(), 4)
        self.assertEqual(Expression("1 * 3").eval(), 3)
        self.assertEqual(Expression("1 + 2 * 3").eval(), 9)
        self.assertEqual(Expression("(1 * 3)").eval(), 3)
        self.assertEqual(Expression("1 + (3*4)").eval(), 13)
        self.assertEqual(Expression("(3+4) * 2").eval(), 14)       

    def test_example_expressions(self):
        self.assertEqual(Expression("1 + (2 * 3) + (4 * (5 + 6))").eval(), 51)
        self.assertEqual(Expression("2 * 3 + (4 * 5)").eval(), 26)
        self.assertEqual(Expression("5 + (8 * 3 + 9 + 3 * 4 * 3)").eval(), 437)
        self.assertEqual(Expression("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))").eval(), 12240)
        self.assertEqual(Expression("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2").eval(), 13632)

    def test_example_expressions_part2(self):
        self.assertEqual(Expression2("1 + (2 * 3) + (4 * (5 + 6))").eval(), 51)
        self.assertEqual(Expression2("2 * 3 + (4 * 5)").eval(), 46)
        self.assertEqual(Expression2("5 + (8 * 3 + 9 + 3 * 4 * 3)").eval(), 1445)
        self.assertEqual(Expression2("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))").eval(), 669060)
        self.assertEqual(Expression2("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2").eval(), 23340)

if __name__ == "__main__": 
    unittest.main()