#!/usr/bin/env python3
from __future__ import annotations
from enum import IntEnum
import re


from typing import Dict, List, Tuple, Optional

from utils import read_inputfile

EdgeSet = List[str]

class Orientation(IntEnum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3 

class Tile:

    def __init__(self, id, lines: List[str]):
        self.cells : List[str] = lines
        self.id = id

    def __eq__(self, other):
        return self.cells == other.cells

    def __repr__(self):
        return str(self.id) + "\n" + "\n".join(self.cells)

    def __hash__(self):
        return hash("".join(self.cells))

    def get_edges(self) -> EdgeSet:
        edges : EdgeSet = []
        top = self.cells[0]
        left = ""
        right = ""
        for line in self.cells:
            left += line[0]
            right += line[len(line)-1]
        bottom = self.cells[len(self.cells)-1]
        # bottom = bottom[::-1]
        # left = left[::-1]
        edges = [top, right, bottom, left]
        return edges

    def count_comon_edges(self, other) -> int:
        same = 0
        for e1 in self.get_edges():
            for e2 in other.get_edges():
                if e1 == e2 or e1 == e2[::-1]:
                    same += 1
        return same

    def rotate(self):
        rotated = [ ("".join(x))[::-1] for x in zip(*self.cells) ]
        return Tile(self.id, rotated)

    def flip_vert(self):
        flipped = [ line[::-1] for line in self.cells ]
        return Tile(self.id, flipped)

    def flip_horiz(self):
        flipped = self.cells[::-1]
        return Tile(self.id, flipped)

    # Return all variants of a tile, e.g. by flipping and/or rotating it
    def get_variants(self):
        result = []
        rotated = self
        for i in range(0, 4):
            result.append(rotated)
            result.append(rotated.flip_vert())
            result.append(rotated.flip_horiz())
            rotated = rotated.rotate()
        return result

    # Finds sea monsters in a tile and marks them with "O", returns the number of monsters found.
    def find_sea_monsters(self):
        monster1 = "                  O "
        monster2 = "O    OO    OO    OOO"
        monster3 = " O  O  O  O  O  O   "
        pattern1 = "([#\s]{18}#[#\s])"
        pattern2 = "(#[#\s]{4}##[#\s]{4}##[#\s]{4}###)"
        pattern3 = "([#\s]#[#\s]{2}#[#\s]{2}#[#\s]{2}#[#\s]{2}#[#\s]{2}#[#\s]{3})"
        monsters = 0
        lines = [ line.replace(".", " ") for line in self.cells ]
        for i in range(1, len(lines)-1):
            for mo2 in re.finditer(pattern2, lines[i]):
                x2 = mo2.start()
                mo3 = re.search(pattern3, lines[i+1][x2:])
                if mo3 is not None:
                    x3 = mo3.start()
                    mo1 = re.search(pattern1, lines[i-1][x2:])
                    if mo1 is not None:
                        x1 = mo1.start()
                        if x1 == 0 and x3 == 0:
                            monsters += 1 
                            lines[i] = lines[i][:x2] + monster2 + lines[i][x2+20:] 
                            lines[i-1] = lines[i-1][:x2] + monster1 + lines[i-1][x2+20:] 
                            lines[i+1] = lines[i+1][:x2] + monster3 + lines[i+1][x2+20:]
        for i in range(0, len(lines)):
            line = lines[i]
            for pos in range(0, len(line)):
                if line[pos] == "O":
                    self.cells[i] = self.cells[i][:pos] + "O" + self.cells[i][pos+1:]
        return monsters

    def count_hashes(self):
        result = 0
        for line in self.cells:
            for ch in line:
                if ch == "#":
                    result += 1
        return result
        

def parse_tiles(input) -> Dict[int, Tile]:
    l= 0
    in_tile = False
    tiles = {}
    tile : List[str] = []
    no = 0
    while l < len(input):
        line = input[l]
        mo = re.match("Tile\s+(\d+):", line)
        if mo is not None:
            no = int(mo.group(1))
            in_tile = True
            tile = []
        elif in_tile:
            if line != "":
                tile.append(line)
            else:
                in_tile = False
                tiles[no] = Tile(no, tile)
        l += 1
    if in_tile:
        tiles[no] = Tile(no, tile)
    return(tiles)

# Finds the corners in the set of tiles -- this works because there is only one single way of
# composing the tiles into the fiinal image
def find_corners(tiles: Dict[int, Tile]) -> List[int]:
    corners = []
    for t1 in tiles:
        sum = 0
        for t2 in tiles:
            if t1 != t2:
                same = tiles[t1].count_comon_edges(tiles[t2])
                sum += same                   
        # print("%d has %d neighbours" % (t1, sum))
        if sum == 2:
            corners.append(t1)
        assert sum <= 4
    # print(corners)
    return corners

# Finds the neighbour tile for some tile, also turns/flips the neighbour in the proper orientation 
def get_neighbour(self, direction, tiles: Dict[int, Tile]) -> Optional[Tile]:
    neighbours : List[int] = []
    for o in tiles:
        other = tiles[o]
        if other.id != self.id:
            if self.count_comon_edges(other) > 0:
                neighbours.append(o)
    # print(neighbours)   
    result = None
    for n in neighbours:
        neighbour = tiles[n]
        variants = neighbour.get_variants()
        if direction == Orientation.UP:
            for variant in variants:
                if variant.get_edges()[Orientation.DOWN] == self.get_edges()[direction]:
                    result = variant
        if direction == Orientation.DOWN:
            for variant in variants:
                if variant.get_edges()[Orientation.UP] == self.get_edges()[direction]:
                    result = variant
        if direction == Orientation.LEFT:
            for variant in variants:
                if variant.get_edges()[Orientation.RIGHT] == self.get_edges()[direction]:
                    result = variant
        if direction == Orientation.RIGHT:
            for variant in variants:
                if variant.get_edges()[Orientation.LEFT] == self.get_edges()[direction]:
                    result = variant
    # print(result)
    return result 

def compute_image(tiles: Dict[int, Tile]):
    image : List[List[Tile]]= []
    # 1. Find the upper, left corner of the composed image
    # The upper left corner can be any of the corners as long as is turned/flipped properly
    corners = find_corners(tiles)
    c = corners[0]
    corner = tiles[c] 
    right = None
    down = None
    for variant in corner.get_variants():
        right = get_neighbour(variant, Orientation.RIGHT, tiles)
        down = get_neighbour(variant, Orientation.DOWN, tiles)  
        if get_neighbour(variant, Orientation.RIGHT, tiles) is not None and get_neighbour(variant, Orientation.DOWN, tiles) is not None:
            down = variant
            # print("Found left, upper corner!")
            break
    j = 0
    # 2. Compose the final image step by step, line by line into an "array" of properly aligned tiles
    while down is not None:
        row = []
        i = 0
        right = down
        while right is not None:
            # print("(%d, %d) = %d" % (j, i, right.id))
            row.append(right)
            right = get_neighbour(right, Orientation.RIGHT, tiles)
            i += 1

        down = get_neighbour(down, Orientation.DOWN, tiles)
        image.append(row)
        j += 1
    # 3. Convert the tiles into a "super" tile
    size = len(image[0][0].cells)
    lines : List[str] = []
    for y in image:
        for i in range(1, size-1):
            line = ""
            for x in y:
                line += x.cells[i][1:size-1]
            lines.append(line)
    result = Tile(0, lines)
    # print(result)
    return result


def part1(input):
    tiles = parse_tiles(input)
    corners = find_corners(tiles)
    result = 1
    for corner in corners:
        result = result * corner
    return result

def part2(input):
    tiles = parse_tiles(input)
    sea = compute_image(tiles)
    result = 0
    for variant in set(sea.get_variants()):
        found = variant.find_sea_monsters()
        if found > 0:
            print(variant)
            result = variant.count_hashes()
    return result

def main():    

    # Official input
    input = read_inputfile("input20.txt")

    print("The solution for part 1 on the official input is %d" % (part1(input)))
    print("The solution for part 2 on the official input is %d" % (part2(input)))

if __name__ == "__main__": 
    main()

