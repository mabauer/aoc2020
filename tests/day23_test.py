#!/usr/bin/env python3

import unittest

from day23 import CupGame, MillionCupGame, MILLION

class Day23Test(unittest.TestCase):

    def test_rotate(self):
        input = "123456789"
        game = CupGame(input)
        game.rotate(-3)
        self.assertEqual(game.get_labeling(), "456789123")
        game.rotate(5)
        self.assertEqual(game.get_labeling(), "891234567")

    def test_cupgame_move(self):
        input = "389125467"
        game = CupGame(input)
        game.make_move()
        self.assertEqual(game.get_labeling(), "328915467")
        
    def test_cupgame_10moves(self):
        input = "389125467"
        game = CupGame(input)
        for i in range(0, 10):
            game.make_move()
        self.assertEqual(game.get_labeling(1), "192658374")

    def test_part1_on_example(self):
        input = "389125467"
        game = CupGame(input)
        for i in range(0, 100):
            game.make_move()
        self.assertEqual(game.get_labeling(1), "167384529")

    def test_millioncupgame_part1_on_example(self):
        input = "389125467"
        game = MillionCupGame(input)
        for i in range(0, 100):
            game.make_move()
        self.assertEqual(game.get_labeling(1), "167384529")

    def test_millioncupgame_part2_on_example(self):
        input = "389125467"
        game = MillionCupGame(input, MILLION)
        for i in range(0, 10*MILLION):
            game.make_move()
        self.assertEqual(game.get_cups_with_stars(), (934001, 159792))

if __name__ == "__main__": 
    unittest.main()