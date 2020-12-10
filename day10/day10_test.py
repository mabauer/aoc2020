#!/usr/bin/env python3

import unittest
import os
import sys

import day10

class Day10Test(unittest.TestCase):

    def test_part1_on_example_a(self):
        input_file = os.path.abspath(os.path.dirname(__file__)) + os.path.sep + "example10a.txt"
        with open(input_file) as f:
            input = [l.strip() for l in f]
         
        adapters = day10.read_numbers(input)
        print(adapters)
        (ones, threes) = day10.find_differences_in_adapter_chain(adapters)
        self.assertEqual((ones, threes), (7, 5))

    def test_find_adapter_chains(self):
        self.assertEqual(day10.find_adapter_chains(0, 0, [3], []), [[0, 3]])
        self.assertEqual(day10.find_adapter_chains(0, 0, [1, 4], []), [[0, 1, 4]])
        self.assertEqual(day10.find_adapter_chains(0, 0, [1, 3, 4], []), [[0, 1, 3, 4], [0, 1, 4], [0, 3, 4]])
        print(day10.find_adapter_chains(0, 0, [1, 4, 5, 6, 7, 10], []))
        print(day10.find_adapter_chains(0, 0, [1, 4, 5, 6, 7, 10, 11, 12, 13], []))
        print(day10.find_adapter_chains(0, 0, [1, 4, 5, 6, 7, 10, 11, 13], []))

        # print(day10.find_adapter_chains(0, 0, [1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19, 22], []))
        # self.assertEqual(day10.find_adapter_chains(0, [1, 4, 5, 6, 7], []), [[0, 1, 4, 5, 7], [0, 1, 4, 6, 7]])

    def test_find_adapter_chains_on_example(self):
        input_file = os.path.abspath(os.path.dirname(__file__)) + os.path.sep + "example10a.txt"
        with open(input_file) as f:
            input = [l.strip() for l in f]

        adapters = day10.read_numbers(input)
        adapters.append(22)
        adapters.sort()
        chains = day10.find_adapter_chains(0, 0, adapters, [])
        print(chains)
        self.assertEquals(len(chains), 8)

    def test_part2_on_example_a(self):
        input_file = os.path.abspath(os.path.dirname(__file__)) + os.path.sep + "example10a.txt"
        with open(input_file) as f:
            input = [l.strip() for l in f]
        
        self.assertEqual(day10.part2(input), 8)

    def test_part2_on_example_b(self):
        input_file = os.path.abspath(os.path.dirname(__file__)) + os.path.sep + "example10b.txt"
        with open(input_file) as f:
            input = [l.strip() for l in f]

        self.assertEqual(day10.part2(input), 19208)

if __name__ == "__main__": 
    unittest.main()