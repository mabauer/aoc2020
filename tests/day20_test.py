#!/usr/bin/env python3

import unittest
import os
import sys

from day20 import compute_edges, count_comon_edges, parse_tiles, part1, part2, find_corners
from utils import read_inputfile

class Day20Test(unittest.TestCase):

    def test_parse_tiles_on_example_data(self):
        input = read_inputfile("example20.txt")
        tiles = parse_tiles(input)
        print(tiles.keys())
        self.assertEqual(len(tiles), 9)

    def test_compute_edges_on_example_data(self):
        input = read_inputfile("example20.txt")
        tiles = parse_tiles(input)
        edges = compute_edges(tiles)
        self.assertEqual(len(edges), 9)
        print(edges.keys())
        self.assertEqual(edges[3079][0], "#.#.#####.")
        self.assertEqual(edges[3079][3], "#..##.#...")
        # self.assertEqual(edges[3079][3], "...#.##..#")

    # def test_rotate_tile(self):
    #     edge_set = ["1", "2", "3", "4"]
    #     self.assertEqual(rotate_tile(edge_set, 2), ["3", "4", "1", "2"])

    def test_count_common_edges(self):
        input = read_inputfile("example20.txt")
        tiles = parse_tiles(input)
        edges = compute_edges(tiles)
        print("Common edges: %s" % count_comon_edges(edges[2971], edges[1489]))

    def test_find_corners(self):
        input = read_inputfile("example20.txt")
        tiles = parse_tiles(input)
        edges = compute_edges(tiles)
        self.assertEqual(find_corners(edges), [1951, 1171, 2971, 3079])

    def test_part1_on_example(self):
        input = read_inputfile("example20.txt")
        self.assertEqual(part1(input), 20899048083289)

    def test_part2(self):
        input = [""]
        self.assertEqual(part2(input), 0)

if __name__ == "__main__": 
    unittest.main()