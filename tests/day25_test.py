#!/usr/bin/env python3

import unittest

from day25 import guess_loop_size, part1, transform

class Day25Test(unittest.TestCase):

    def test_transform(self):
        self.assertEqual(transform(7, 8), 5764801)
        self.assertEqual(transform(7, 11), 17807724)
        self.assertEqual(transform(17807724, 8), 14897079)
        self.assertEqual(transform(5764801, 11), 14897079)

    def test_guess_loop_size(self):
        self.assertEqual(guess_loop_size(5764801), 8)
        self.assertEqual(guess_loop_size(17807724), 11)

    def test_part1_on_example_data(self):
        input = (5764801, 17807724)
        self.assertEqual(part1(input), 14897079)

if __name__ == "__main__": 
    unittest.main()