#!/usr/bin/env python3

import unittest

from day22 import RecursiveGame, part1, part2
from utils import read_inputfile

class Day22Test(unittest.TestCase):

    def test_part1_on_example_data(self):
        input = read_inputfile("example22.txt")
        self.assertEqual(part1(input), 306)

    def test_part2_on_example_data(self):
        input = read_inputfile("example22.txt")
        self.assertEqual(part2(input), 291)

    def test_part2_on_infinite_example(self):
        deck_player1 = [43, 19]
        deck_player2 = [2, 29, 14]
        game = RecursiveGame([deck_player1, deck_player2], debug=True)
        game.play()

if __name__ == "__main__": 
    unittest.main()