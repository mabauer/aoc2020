#!/usr/bin/env python3

import re
import os
import sys

from typing import List

OCCUPIED = "#"
EMPTY = "L"

class Game:

    def __init__(self, lines: List[str]):
        self.cells : List[str] = []
        self.y_max = len(lines)-1
        self.x_max = len(lines[0])-1
        for line in lines:
            self.cells.append(line)
    
    def next_generation(self) -> bool:
        changed = False
        number_of_neighbours : List[List[int]]= []
        for y in range(0, len(self.cells)):
            line : List[int] = []
            for x in range(0, len(self.cells[y])):
                line.append(self.count_neighbours(x, y))
            number_of_neighbours.append(line)
        for y in range(0, len(self.cells)):
            for x in range(0, len(self.cells[y])):
                c = number_of_neighbours[y][x]
                if self.get_cell(x, y) == OCCUPIED and c >= 4:
                    self.set_cell(x, y, EMPTY)
                    changed = True
                if self.get_cell(x, y) == EMPTY and c == 0:
                    self.set_cell(x, y, OCCUPIED)
                    changed = True 
        return changed

    def get_cell(self, x: int, y: int)  -> str:
        return self.cells[y][x]       

    def set_cell(self, x: int, y: int, value: str):
        self.cells[y] = self.cells[y][:x] + value + self.cells[y][x+1:]

    def count_neighbours(self, x: int, y: int) -> int:
        result = 0
        # Left upper neighbour
        if x-1 >= 0 and y-1 >= 0 and self.get_cell(x-1, y-1) == OCCUPIED:
            result += 1
        # Middle upper neighbour
        if y-1 >= 0 and self.get_cell(x, y-1) == OCCUPIED: 
            result += 1
        # Right upper neighbour
        if x+1 <= self.x_max and y-1 >= 0 and self.get_cell(x+1, y-1) == OCCUPIED: 
            result += 1
        # Left neigbour
        if x-1 >= 0 and self.get_cell(x-1, y) == OCCUPIED:
            result += 1
        # Right neighbour
        if x+1 <= self.x_max and self.get_cell(x+1, y) == OCCUPIED:
            result += 1
        # Lower left neighbour
        if x-1 >= 0 and y+1 <= self.y_max and self.get_cell(x-1, y+1) == OCCUPIED:
            result += 1
        # Lower neighbour
        if y+1 <= self.y_max and self.get_cell(x, y+1) == OCCUPIED:
            result += 1
        # Lower right neighbour
        if y+1 <= self.y_max and x+1 <= self.x_max and self. get_cell(x+1, y+1) == OCCUPIED:
            result += 1
        return result

    def count_occupied_seats(self):
        result = 0
        for line in self.cells:
            result += line.count(OCCUPIED)
        return result

    def print(self):
        for line in self.cells:
            print(line)

def part1(input):
    game = Game(input)
    gens = 0
    while game.next_generation():
        gens += 1
        game.print()
        print()
    print("Stable after %d generations." % gens)
    result = game.count_occupied_seats()
    return result


def part2(input):
    result = 0
    return result

def main():    

    # Official input
    input_file = os.path.abspath(os.path.dirname(__file__)) + os.path.sep + "input11.txt"
    with open(input_file) as f:
        input = [l.strip() for l in f]

    print("The solution for part 1 on the official input is %d" % (part1(input)))
    print("The solution for part 2 on the official input is %d" % (part2(input)))

if __name__ == "__main__": 
    main()

