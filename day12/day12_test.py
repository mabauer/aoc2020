#!/usr/bin/env python3

import unittest
import os
import sys

from day12 import Ship
from day12 import rotate_point
from day12 import rotate_point_by_90s

class Day12Test(unittest.TestCase):

    def test_part1(self):
        input = ["F10", "N3", "F7", "R90", "F11"]
        ship = Ship()
        ship.print()
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

    def test_part2(self):
        input = ["F10", "N3", "F7", "R90", "F11"]
        ship = Ship()
        ship.turnon_waypoint(10, 1)
        ship.print()
        ship.navigate(input)
        self.assertEqual(ship.x, 214)
        self.assertEqual(ship.y, -72)
        self.assertEqual(ship.compute_distance(), 286)

    def test_part2_turn_left(self):
        input = ["F10", "L180", "F10"]
        ship = Ship()
        ship.turnon_waypoint(10, 1)
        ship.print()
        ship.navigate(input)
        self.assertEqual(ship.x, 0)
        self.assertEqual(ship.y, 0)

    def test_rotate_waypoint(self):
        ship = Ship(170, 38)
        ship.turnon_waypoint(10, 4)
        ship.turn_right(90)
        self.assertEqual(ship.x, 170)
        self.assertEqual(ship.y, 38)
        self.assertEqual(ship.wp_x, 4)
        self.assertEqual(ship.wp_y, -10)
        ship.go_forward(11)
        self.assertEqual(ship.x, 214)
        self.assertEqual(ship.y, -72)
        self.assertEqual(ship.compute_distance(), 286)

    def test_rotate_point(self):
        p1 = (-2, 15)
        self.assertEqual(rotate_point(p1, -90), (15, 2))
        self.assertEqual(rotate_point_by_90s(p1, -90), (15, 2))


    def test_rotate_waypoint_special_cases(self):
        ship = Ship(0, 0)
        ship.turnon_waypoint(1, 0)
        ship.turn_left(90)
        self.assertEqual(ship.wp_x, 0)
        self.assertEqual(ship.wp_y, 1)
        ship.turn_left(90)
        self.assertEqual(ship.wp_x, -1)
        self.assertEqual(ship.wp_y, 0)
 
if __name__ == "__main__": 
    unittest.main()