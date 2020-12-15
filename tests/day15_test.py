#!/usr/bin/env python3

import unittest


from day15 import play

class Day15Test(unittest.TestCase):

    def test_play_on_example_data(self):
        input = [0,3,6]
        self.assertEqual(play(input, 10), 0)

    def test_play_more_examples(self):
        self.assertEqual(play([1,3,2]), 1)
        self.assertEqual(play([2,1,3]), 10)
        self.assertEqual(play([1,2,3]), 27)
        self.assertEqual(play([2,3,1]), 78)
        self.assertEqual(play([3,2,1]), 438)
        self.assertEqual(play([3,1,2]), 1836)

    def test_play_examples_part_2(self):
        # These tests run a long time, to activate set long_running = True
        long_running = False
        if long_running:
            self.assertEqual(play([0,3,6], 30000000), 175594)
            self.assertEqual(play([1,3,2], 30000000), 2578)
            self.assertEqual(play([2,1,3], 30000000), 3544142)
            self.assertEqual(play([1,2,3], 30000000), 261214)
            self.assertEqual(play([2,3,1], 30000000), 6895259)
            self.assertEqual(play([3,2,1], 30000000), 18)
            self.assertEqual(play([3,1,2], 30000000), 362)

if __name__ == "__main__": 
    unittest.main()