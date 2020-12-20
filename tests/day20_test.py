#!/usr/bin/env python3

import unittest
import os
import sys

from day20 import Orientation, Tile, compute_image, parse_tiles, part1, part2, find_corners
from utils import read_inputfile

class Day20Test(unittest.TestCase):

    def test_parse_tiles_on_example_data(self):
        input = read_inputfile("example20.txt")
        tiles = parse_tiles(input)
        # print(tiles.keys())
        self.assertEqual(len(tiles), 9)

    def test_compute_edges_on_example_data(self):
        input = read_inputfile("example20.txt")
        tiles = parse_tiles(input)
        edgeset = tiles[3079].get_edges()
        self.assertEqual(edgeset[Orientation.UP], "#.#.#####.")
        self.assertEqual(edgeset[Orientation.LEFT], "#..##.#...")

    def test_count_common_edges(self):
        input = read_inputfile("example20.txt")
        tiles = parse_tiles(input)
        self.assertEqual(tiles[2971].count_comon_edges(tiles[1489]), 1)

    def test_rotate(self):
        tile = Tile(0, ["123", "456", "789"])
        rotated_tile = tile.rotate()
        # print(rotated_tile)
        self.assertEqual(rotated_tile.cells, ['741', '852', '963'])

    def test_flip_vert(self):
        tile = Tile(0, ["123", "456", "789"])
        flipped_tile = tile.flip_vert()
        print(flipped_tile.cells)
        self.assertEqual(flipped_tile.cells, ['321', '654','987'])
        self.assertEqual(flipped_tile.flip_vert(), tile)

    def test_flip_horiz(self):
        tile = Tile(0, ["123", "456", "789"])
        flipped_tile = tile.flip_horiz()
        print(flipped_tile.cells)
        self.assertEqual(flipped_tile.cells, ['789', '456', '123'])
        self.assertEqual(flipped_tile.flip_horiz(), tile)

    def test_get_variants(self):
        input = read_inputfile("example20.txt")
        tiles = parse_tiles(input)
        variants = tiles[3079].get_variants()
        for tile in variants:
            print(tile)
            print()
        print("Variants: %d, %d unique." % (len(variants), len(set(variants))))

    def test_find_corners(self):
        input = read_inputfile("example20.txt")
        tiles = parse_tiles(input)
        self.assertEqual(find_corners(tiles), [1951, 1171, 2971, 3079])

    def test_compute_image(self):
        # input = read_inputfile("input20.txt")
        input = read_inputfile("example20.txt")
        tiles = parse_tiles(input)
        image = compute_image(tiles)
        #print(image)
        solution = read_inputfile("example20solution.txt")
        expected = Tile(0, solution)
        self.assertIn(image, expected.get_variants())

    def test_find_sea_monsters(self):
        input = read_inputfile("example20b.txt")
        sea = Tile(0, input)
        self.assertEqual(sea.find_sea_monsters(), 2)
        self.assertEqual(sea.count_hashes(), 273)
        

    def test_part1_on_example(self):
        input = read_inputfile("example20.txt")
        self.assertEqual(part1(input), 20899048083289)

    def test_part2(self):
        input = read_inputfile("example20.txt")
        self.assertEqual(part2(input), 273)

if __name__ == "__main__": 
    unittest.main()