#!/usr/bin/env python3

import unittest
import os
import sys

import day07

class Day07Test(unittest.TestCase):

    def test_part1_on_example_data(self):
        input_file = os.path.abspath(os.path.dirname(__file__)) + os.path.sep + "example07.txt"
        with open(input_file) as f:
            input = [x.strip() for x in f]
        graph = day07.build_graph_from_rules(input)
        # print(graph)
        # print(graph.find_all_reachable_nodes("shinygold"))
        self.assertEqual(len(graph.find_all_reachable_nodes("shinygold")),  4)

    def test_part2_on_example_data(self):
        input_file = os.path.abspath(os.path.dirname(__file__)) + os.path.sep + "example07.txt"
        with open(input_file) as f:
            input = [x.strip() for x in f]
        graph = day07.build_graph_from_rules(input, use_contains=True)
        # print(graph)
        self.assertEqual(day07.count_all_bags_recursively(graph, "shinygold")-1, 32)

    def test_part2(self):
        input = [
            "shiny gold bags contain 2 dark red bags.",
            "dark red bags contain 2 dark orange bags.",
            "dark orange bags contain 2 dark yellow bags.",
            "dark yellow bags contain 2 dark green bags.",
            "dark green bags contain 2 dark blue bags.",
            "dark blue bags contain 2 dark violet bags.",
            "dark violet bags contain no other bags."
        ]
        graph = day07.build_graph_from_rules(input, use_contains=True)
        self.assertEqual(day07.count_all_bags_recursively(graph, "shinygold")-1, 126)


if __name__ == "__main__": 
    unittest.main()