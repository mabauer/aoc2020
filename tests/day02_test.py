#!/usr/bin/env python3

import unittest

from day02 import count_valid_passwds, is_valid_passwd_part1, is_valid_passwd_part2 

class DayXXTest(unittest.TestCase):

    def test_part1_on_example_data(self):
        # Example data
        input = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]
        self.assertEqual(count_valid_passwds(input, is_valid_passwd_part1), 2)

    def test_part2_on_example_data(self):
        input = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]
        self.assertEqual(count_valid_passwds(input, is_valid_passwd_part2), 1)

if __name__ == "__main__": 
    unittest.main()