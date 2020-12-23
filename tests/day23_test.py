#!/usr/bin/env python3

import unittest
import os
import sys

from day23 import CupGame, part1, part2
from utils import read_inputfile

class Day23Test(unittest.TestCase):

    def test_rotate(self):
        input = "123456789"
        game = CupGame(input)
        game.rotate(-3)
        self.assertEqual(game.get_labeling(), "456789123")
        game.rotate(5)
        self.assertEqual(game.get_labeling(), "891234567")

    def test_part1_move(self):
        input = "389125467"
        game = CupGame(input)
        game.make_move()
        self.assertEqual(game.get_labeling(), "328915467")
        
    def test_part1_10moves(self):
        input = "389125467"
        game = CupGame(input)
        for i in range(0, 10):
            game.make_move()
        #self.assertEqual(game.get_labeling(), "583741926")
        self.assertEqual(game.get_labeling(1), "192658374")

    def test_part1(self):
        input = "389125467"
        game = CupGame(input)
        for i in range(0, 100):
            game.make_move()
        #self.assertEqual(game.get_labeling(), "583741926")
        self.assertEqual(game.get_labeling(1), "167384529")

    def test_part2(self):
        input = [""]
        self.assertEqual(part2(input), 0)

if __name__ == "__main__": 
    unittest.main()