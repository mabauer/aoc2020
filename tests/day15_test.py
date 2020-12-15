#!/usr/bin/env python3

import unittest


from day15 import play

class Day15Test(unittest.TestCase):

    def test_play_on_example_data(self):
        input = [0,3,6]
        self.assertEqual(play(input, 10), 0)

    def test_play(self):
        self.assertEqual(play([1,3,2]), 1)
        self.assertEqual(play([2,1,3]), 10)


if __name__ == "__main__": 
    unittest.main()