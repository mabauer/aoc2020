#!/usr/bin/env python3

import re
import os
import sys
import math
from typing import List

class Ship:

    def __init__(self, x: int = 0, y: int = 0, orientation: int = 0):
        self.x = x
        self.y = y
        self.orientation = orientation

    def go_north(self, distance: int):
        self.y += distance

    def go_south(self, distance: int):
        self.y -= distance

    def go_east(self, distance: int):
        self.x += distance

    def go_west(self, distance: int):
        self.x -= distance

    def turn_left(self, degrees: int):  
        self.orientation += degrees

    def turn_right(self, degrees: int):
        self.orientation -= degrees

    def go_forward(self, distance: int):
        rad = float(self.orientation) * math.pi / 180
        dx = round(math.cos(rad) * distance)
        dy = round(math.sin(rad) * distance)
        self.x += dx
        self.y += dy
        print("go_forward by (%d, %d) to (%d, %d)" % (dx, dy, self.x, self.y))


    def compute_distance(self):
        return abs(self.x) + abs(self.y)

    def navigate(self, input: List[str]):
        for instruction in input:
            cmd = instruction[0]
            value = int(instruction[1:])
            print("%s %d" % (cmd, value))
            if cmd == "N":
                self.go_north(value)
            if cmd == "S":
                self.go_south(value)
            if cmd == "E":
                self.go_east(value)
            if cmd == "W":
                self.go_west(value)
            if cmd == "L":
                self.turn_left(value)
            if cmd == "R":
                self.turn_right(value)
            if cmd == "F":
                self.go_forward(value)
            self.print()
    
    def print(self):
        print("Ship: (%d %d), orientation: %d" % (self.x, self.y, self.orientation))

            
def part1(input):
    ship = Ship()
    ship.navigate(input)
    result = ship.compute_distance()
    return result

def part2(input):
    result = 0
    return result

def main():    

    # Official input
    input_file = os.path.abspath(os.path.dirname(__file__)) + os.path.sep + "input12.txt"
    with open(input_file) as f:
        input = [l.strip() for l in f]

    print("The solution for part 1 on the official input is %d" % (part1(input)))
    print("The solution for part 2 on the official input is %d" % (part2(input)))

if __name__ == "__main__": 
    main()

