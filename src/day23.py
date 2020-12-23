#!/usr/bin/env python3

import re
import os
import sys

# from utils import read_inputfile
from typing import List, Sized

class CupGame:

    def __init__(self, s : str):
        self.cups : List[int] = [ int(c) for c in s ]
        self.size = len(self.cups)
        self.current_position = -1
        self.move = 0

    def pickup(self) -> List[int]:
        i = 1
        result = []
        while i < 4:
            result.append(self.cups[(self.current_position + i) % self.size])
            i += 1
        return result

    def destination(self, picks) -> int:
        current_cup = self.cups[self.current_position]
        destination_cup = current_cup - 1
        if destination_cup < min(self.cups):
            destination_cup = max(self.cups)
        while destination_cup in picks:
            destination_cup -= 1
            if destination_cup < min(self.cups):
                destination_cup = max(self.cups)
        destination = self.cups.index(destination_cup)
        return destination

    def rotate(self, count : int):
        temp = []
        for i in range (0, self.size):
            pos = i - count
            if pos < 0:
                pos = self.size + pos
            if pos >= self.size:
                pos = pos % self.size 
            temp.append(self.cups[pos])
        self.cups = temp

    def place_pickup(self, picks: List[int], destination):
        old_pos = self.current_position
        for p in picks:
            pos = self.cups.index(p)
            if pos < self.current_position:
                self.current_position -= 1
            if pos < destination:
                destination -= 1
            self.cups.remove(p)
        for p in reversed(picks):
            self.cups.insert(destination + 1, p)
            if destination < self.current_position:
                self.current_position += 1
        print("Rotation: %d" % (self.current_position - old_pos))

    def print_move(self, picks : List[int], destination: int):
        print("-- move %d --" % self.move)
        print("cups: ", end="")
        for i in range(0, len(self.cups)):
            if i != self.current_position:
                print(" %d " % self.cups[i], end="")
            else:
                print("(%d)" % self.cups[i], end = "")
        print()
        print("pickup: %s" % (", ".join([str(i) for i in picks])))
        print("destination: %d" % self.cups[destination])

    def make_move(self):
        self.move += 1
        self.current_position = (self.current_position + 1) % self.size
        picks = self.pickup()
        destination = self.destination(picks)
        self.print_move(picks, destination)
        self.place_pickup(picks, destination)

    def get_labeling(self, start=0):
        pos = 0
        if start != 0:
            pos = self.cups.index(start)
        labels = [ str(self.cups[i % self.size]) for i in range(pos, pos + self.size) ]
        return "".join(labels)


def part1(input):
    game = CupGame(input)
    for i in range(0, 100):
        game.make_move()
    result = game.get_labeling(1)[1:]
    return result

def part2(input):
    result = 0
    return result

def main():    

    # Official input
    input = "158937462"

    print("The solution for part 1 on the official input is %s" % (part1(input)))
    print("The solution for part 2 on the official input is %d" % (part2(input)))

if __name__ == "__main__": 
    main()

