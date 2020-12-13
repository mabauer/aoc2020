#!/usr/bin/env python3

import unittest
import os
import sys

from day13 import buses_in_service, part1, part2
from utils import read_inputfile

class Day13Test(unittest.TestCase):

    def test_buses_in_service(self):
        input = "7,13,x,x,59,x,31,19"
        buses = buses_in_service(input)
        self.assertEqual(sorted(buses), [7, 13, 19, 31, 59])

    def test_part1_on_example_data(self):
        input = read_inputfile("example13.txt")
        self.assertEqual(part1(input), 295)

    def test_part2(self):
        s = "17,x,13,19"
        self.assertEqual(part2(s), 3417)
        s = "67,7,59,61"
        self.assertEqual(part2(s), 754018)
        s = "67,x,7,59,61"
        self.assertEqual(part2(s), 779210)
        s = "67,7,x,59,61"
        self.assertEqual(part2(s), 1261476)
        s = "1789,37,47,1889"
        self.assertEqual(part2(s), 1202161486)

    def test_part2_on_example_data(self):
        input = read_inputfile("example13.txt")
        self.assertEqual(part2(input[1]), 1068781)

if __name__ == "__main__": 
    unittest.main()