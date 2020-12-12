#!/usr/bin/env python3

import unittest
import os
import sys

from day12 import Ship

class Day12Test(unittest.TestCase):

    def test_part1(self):
        input = ["F10", "N3", "F7", "R90", "F11"]
        ship = Ship()
        ship.navigate(input)
        self.assertEqual(ship.x, 17)
        self.assertEqual(ship.y, -8)
        self.assertEqual(ship.compute_distance(), 25)

    def test_turn_right(self):
        ship = Ship(17, 3, 0)
        ship.turn_right(90)
        ship.go_forward(11)
        self.assertEqual(ship.x, 17)
        self.assertEqual(ship.y, -8)
        self.assertEqual(ship.compute_distance(), 25)




    # def test_part1_on_example_data(self):
    #     input_file = os.path.abspath(os.path.dirname(__file__)) + os.path.sep + "example12.txt"
    #     with open(input_file) as f:
    #         input = [l.strip() for l in f]
    #     self.assertEqual(day12.part1(input), 0)

    def test_part2(self):
        input = [""]
        # self.assertEqual(day12.part2(input), 0)

if __name__ == "__main__": 
    unittest.main()