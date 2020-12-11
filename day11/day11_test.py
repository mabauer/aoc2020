#!/usr/bin/env python3

import unittest
import os
import sys

from day11 import Game
from day11 import part1
from day11 import part2

class Day11Test(unittest.TestCase):

    def test_set_cell(self):
        game = Game([
            "#.##.##.##", 
            "#######.##", 
            "#.#.#..#.."
            ])
        game.set_cell(1, 1, "L")
        self.assertEqual(game.cells, [
            "#.##.##.##", 
            "#L#####.##", 
            "#.#.#..#.."
            ])
    def test_count_occupied_neighbours(self):
        game = Game([
            "#.##.##.##", 
            "#######.##", 
            "#.#.#..#.."
            ])
        self.assertEqual(game.count_occupied_neighbours(1, 1), 6)
        self.assertEqual(game.count_occupied_neighbours(0, 0), 2)
        self.assertEqual(game.count_occupied_neighbours(1, 0), 5)
        self.assertEqual(game.count_occupied_neighbours(0, 1), 3)
        self.assertEqual(game.count_occupied_neighbours(9, 0), 3)

    def test_count_visible_occupied_seats(self):
        input_file = os.path.abspath(os.path.dirname(__file__)) + os.path.sep + "example11b.txt"
        with open(input_file) as f:
            input = [l.strip() for l in f]
        game : Game = Game(input)
        self.assertEqual(game.count_visible_occupied_seats(3, 4), 8)

    def test_part1_on_example_data(self):
        input_file = os.path.abspath(os.path.dirname(__file__)) + os.path.sep + "example11a.txt"
        with open(input_file) as f:
            input = [l.strip() for l in f]
        self.assertEqual(part1(input), 37)

    def test_part2_on_example_data(self):
        input_file = os.path.abspath(os.path.dirname(__file__)) + os.path.sep + "example11a.txt"
        with open(input_file) as f:
            input = [l.strip() for l in f]
        self.assertEqual(part2(input), 26)

if __name__ == "__main__": 
    unittest.main()