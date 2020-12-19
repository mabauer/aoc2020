#!/usr/bin/env python3

import re
from typing import List
import unittest

from day19_regex import evaluate_rule, parse_rule, parse_rules, part1, part2
from utils import read_inputfile

class Day19RegexTest(unittest.TestCase):

    def test_parse_rule(self):
        self.assertEqual(parse_rule("0: 4 1 5"), (0, [[4, 1, 5]]))
        self.assertEqual(parse_rule("2: 4 4 | 5 5"), (2, [[4, 4], [5, 5]]))

    def test_parse_rules(self):
        input = read_inputfile("example19a.txt")
        (rules, patterns) = parse_rules(input)
        self.assertEqual(patterns, {1: 'a', 3: 'b'})
        self.assertEqual(rules[0], [[1, 2]])
        self.assertEqual(rules[2], [[1, 3], [3, 1]])

    def test_evaluate_rules_example_a(self):
        input = read_inputfile("example19a.txt")
        (rules, patterns) = parse_rules(input)
        self.assertEqual(evaluate_rule(1, rules, patterns), "a")
        self.assertEqual(evaluate_rule(2, rules, patterns), "((ab)|(ba))")
        self.assertEqual(evaluate_rule(0, rules, patterns), "((a((ab)|(ba))))")

    def test_evaluate_rules_example_b(self):
        input = read_inputfile("example19b.txt")
        (rules, patterns) = parse_rules(input)
        pattern = evaluate_rule(0, rules, patterns)
        print(pattern)
        self.assertTrue(self.can_be_verified("aaaabb", pattern))
        self.assertTrue(self.can_be_verified("aaabab", pattern))
        self.assertTrue(self.can_be_verified("abbabb", pattern))
        self.assertTrue(self.can_be_verified("abbbab", pattern))
        self.assertTrue(self.can_be_verified("aabaab", pattern))
        self.assertTrue(self.can_be_verified("aabbbb", pattern))
        self.assertTrue(self.can_be_verified("abaaab", pattern))
        self.assertTrue(self.can_be_verified("ababbb", pattern))

    def test_part1_on_example_data_b(self):
        input = read_inputfile("example19b.txt")
        self.assertEqual(part1(input), 2)

    def test_part1_on_example_data_c(self):
        input = read_inputfile("example19c.txt")
        self.assertEqual(part1(input), 3)

    def can_be_verified(self, s: str, pattern: str) -> bool:
        if re.fullmatch(pattern, s):
            return True
        return False    

    def test_part2_on_example_data_c(self):
        input = read_inputfile("example19c.txt")
        self.assertEqual(part2(input), 12)

    def test_part2_on_example_data_c_words(self):
        input = read_inputfile("example19c.txt")  
        (rules, patterns) = parse_rules(input)

        rules[8] = [ [ 42 ]*i for i in range(1, 10) ]
        rules[11] = [ [ 42]*i + [31]*i for i in range(1, 10) ]
        
        pattern = evaluate_rule(0, rules, patterns)

        self.assertTrue(self.can_be_verified("bbabbbbaabaabba", pattern))
        self.assertTrue(self.can_be_verified("babbbbaabbbbbabbbbbbaabaaabaaa", pattern))



if __name__ == "__main__": 
    unittest.main()