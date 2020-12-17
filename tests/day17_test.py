#!/usr/bin/env python3

import unittest
import os
import sys

from day17 import Game3D, part1, part2
from utils import read_inputfile

class Day17Test(unittest.TestCase):

    def test_cells(self):
        input = [".#.", "..#", "###"]
        game = Game3D(input)
        game.print()
        self.assertEqual(game.count_active_cells(), 5)
        self.assertEqual(game.count_active_neighbours(0, 0, 0), 5)
        self.assertEqual(game.count_active_neighbours(-1,-1, 0), 1)
        self.assertEqual(game.count_active_neighbours(-1, 0, -1), 3)
        self.assertEqual(game.count_active_neighbours(1, 1, -1), 3)


    def test_example_part1(self):
        input = [".#.", "..#", "###"]
        self.assertEqual(part1(input, 6), 112)
    
    def test_example_part2(self):
        input = [".#.", "..#", "###"]
        self.assertEqual(part2(input), 848)

if __name__ == "__main__": 
    unittest.main()