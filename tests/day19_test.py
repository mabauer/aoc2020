#!/usr/bin/env python3

import unittest

from day19 import append_patterns, evaluate_rule, parse_rule, parse_rules, part1, part2
from utils import read_inputfile

class Day19Test(unittest.TestCase):

    def test_parse_rule(self):
        self.assertEqual(parse_rule("0: 4 1 5"), (0, [[4, 1, 5]]))
        self.assertEqual(parse_rule("2: 4 4 | 5 5"), (2, [[4, 4], [5, 5]]))

    def test_parse_rules(self):
        input = read_inputfile("example19a.txt")
        (rules, patterns) = parse_rules(input)
        self.assertEqual(patterns, {1: ['a'], 3: ['b']})
        self.assertEqual(rules[0], [[1, 2]])
        self.assertEqual(rules[2], [[1, 3], [3, 1]])

    def test_append_patterns(self):
        self.assertEqual(append_patterns(["aa", "ab"], ["ba", "bb"]), ["aaba", "aabb", "abba", "abbb"])

    def test_evaluate_rules_example_a(self):
        input = read_inputfile("example19a.txt")
        (rules, patterns) = parse_rules(input)
        self.assertEqual(evaluate_rule(1, rules, patterns), ["a"])
        self.assertEqual(evaluate_rule(2, rules, patterns), ["ab", "ba"])
        self.assertEqual(evaluate_rule(0, rules, patterns), ["aab", "aba"])

    def test_evaluate_rules_example_b(self):
        input = read_inputfile("example19b.txt")
        (rules, patterns) = parse_rules(input)
        self.assertEqual(evaluate_rule(0, rules, patterns), 
            ["aaaabb", "aaabab", "abbabb", "abbbab", "aabaab", "aabbbb", "abaaab", "ababbb"])

    def test_part1_on_example_data_b(self):
        input = read_inputfile("example19b.txt")
        self.assertEqual(part1(input), 2)

    def test_part2(self):
        input = [""]
        self.assertEqual(part2(input), 0)

if __name__ == "__main__": 
    unittest.main()