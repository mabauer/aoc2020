#!/usr/bin/env python3

import re
import os
import sys
import math
from typing import List
from typing import Tuple

from utils import read_inputfile

# Rotate a point around the origin (by an aritrary angle)
def rotate_point(point: Tuple[int, int], angle: int) -> Tuple[int, int]:
    (x, y) = point
    # Convert point into polar coordinates... 
    # Special cases
    if x == 0:
        if y > 0:
            alpha = 0.5 * math.pi
        else:
            alpha = 1.5 * math.pi 
    else:
        alpha = math.atan2(float(y), float(x)) 
    distance = math.sqrt(x*x + y*y)
    # ...add the angle...
    new_alpha = alpha + math.radians(angle) # or: new_alpha = alpha + (float(angle) * math.pi / 180)
    # ...and convert it back to cartesian coordinates
    x = round(math.cos(new_alpha) * distance)
    y = round(math.sin(new_alpha) * distance)
    return (x, y)

# Rotate a point around the origin (by fixed angles 0, 90, 180, 270,...)
def rotate_point_by_90s(point: Tuple[int, int], angle: int) -> Tuple[int, int]:
    (x, y) = point
    # Make shure angle is between 0..360
    my_angle = math.fmod(angle, 360)
    if my_angle < 0:
        my_angle = 360 + my_angle
    if my_angle not in [0, 90, 180, 270]:
        msg = "Illegal rotation angle: {angle}!"
        raise ValueError(msg.format(angle=angle))
    if my_angle == 90:
        (x, y) = (-y, x)
    if my_angle == 180:
        (x, y) = (-x, -y)
    if my_angle == 270:
        (x, y) = (y, -x)
    return (x, y)
    

class Ship:

    def __init__(self, x: int = 0, y: int = 0, orientation: int = 0):
        self.x = x
        self.y = y
        self.orientation = orientation
        self.use_waypoint = False
        self.wp_x = 0
        self.wp_y = 0

    # This switches the ship into waypoint navigation, see part 2
    def turnon_waypoint(self, x: int, y: int):
        self.use_waypoint = True
        self.wp_x = x
        self.wp_y = y

    def go_north(self, distance: int):
        if self.use_waypoint:
            self.wp_y += distance
        else:
            self.y += distance

    def go_south(self, distance: int):
        if self.use_waypoint:
            self.wp_y -= distance
        else:
            self.y -= distance

    def go_east(self, distance: int):
        if self.use_waypoint:
            self.wp_x += distance
        else:
            self.x += distance

    def go_west(self, distance: int):
        if self.use_waypoint:
            self.wp_x -= distance
        else:
            self.x -= distance

    def turn_left(self, degrees: int):  
        if self.use_waypoint:
            p1 = rotate_point((self.wp_x, self.wp_y), degrees)
            p2 = rotate_point_by_90s((self.wp_x, self.wp_y), degrees)
            if p1 != p2:
                msg = "Left rotation of ({x}, {y}) by {angle} failed!" 
                raise ValueError(msg.format(x=self.wp_x, y=self.wp_y, angle=degrees))
            (self.wp_x, self.wp_y) = p1
        else:    
            self.orientation += degrees

    def turn_right(self, degrees: int):
        if self.use_waypoint:
            p1 = rotate_point((self.wp_x, self.wp_y), -degrees)
            p2 = rotate_point_by_90s((self.wp_x, self.wp_y), -degrees)
            if p1 != p2:
                msg = "Right rotation of ({x}, {y}) by {angle} failed!" 
                raise ValueError(msg.format(x=self.wp_x, y=self.wp_y, angle=degrees))
            (self.wp_x, self.wp_y) = p1
        else:    
            self.orientation -= degrees

    def go_forward(self, distance: int):
        if self.use_waypoint:
            dx = self.wp_x * distance
            dy = self.wp_y * distance
        else:
            rad = math.radians(float(self.orientation)) # rad = float(self.orientation) * math.pi / 180
            dx = round(math.cos(rad) * distance)
            dy = round(math.sin(rad) * distance)
        self.x += dx
        self.y += dy
        # print("go_forward by (%d, %d) to (%d, %d)" % (dx, dy, self.x, self.y))

    def compute_distance(self):
        return abs(self.x) + abs(self.y)

    def navigate(self, input: List[str]):
        for instruction in input:
            cmd = instruction[0]
            value = int(instruction[1:])
            # print("%s %d" % (cmd, value))
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
            # self.print()
    
    def print(self):
        if self.use_waypoint:
            print("Ship: (%d %d), with waypoint at relative (%d, %d)" 
                % (self.x, self.y, self.wp_x, self.wp_y))
        else:
            print("Ship: (%d %d), orientation: %d" % (self.x, self.y, self.orientation))

            
def part1(input):
    ship = Ship()
    # ship.print()
    ship.navigate(input)
    result = ship.compute_distance()
    return result

def part2(input):
    ship = Ship()
    ship.turnon_waypoint(10, 1)
    # ship.print()
    ship.navigate(input)
    result = ship.compute_distance()
    return result

def main():    

    # Official input
    input = read_inputfile("input12.txt")

    print("The solution for part 1 on the official input is %d" % (part1(input)))
    print("The solution for part 2 on the official input is %d" % (part2(input)))

if __name__ == "__main__": 
    main()

