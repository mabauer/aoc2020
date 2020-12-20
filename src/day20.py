#!/usr/bin/env python3

import re

from typing import Dict, List
from itertools import permutations

from utils import read_inputfile

Tile = List[str]
Edges = List[str]

def parse_tiles(input) -> Dict[int, Tile]:
    l= 0
    in_tile = False
    tiles = {}
    tile : Tile = []
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
                tiles[no] = tile
        l += 1
    if in_tile:
        tiles[no] = tile
    return(tiles)

def compute_edges(tiles: Dict[int, Tile]) -> Dict[int, Edges]:
    result : Dict[int, Edges] = {}
    for no in tiles:
        tile = tiles[no]
        edges : Edges = []
        top = tile[0]
        left = ""
        right = ""
        for line in tile:
            left += line[0]
            right += line[len(line)-1]
        bottom = tile[len(tile)-1]
        # bottom = bottom[::-1]
        # left = left[::-1]
        edges = [top, right, bottom, left]
        result[no] = edges
    return result

# def rotate_tile(edge_set: Edges, pos: int) -> Edges:
#     return edge_set[pos:] + edge_set[0:pos]

def count_comon_edges(edge_set1: Edges, edge_set2: Edges):
    same = 0
    for e1 in edge_set1:
        for e2 in edge_set2:
            if e1 == e2 or e1 == e2[::-1]:
                same += 1
    return same

def find_corners(edges: Dict[int, Edges]) -> List[int]:
    corners = []
    for es1 in edges:
        sum = 0
        for es2 in edges:
            if es1 != es2:
                same = count_comon_edges(edges[es1], edges[es2])
                sum += same                   
        # print("%d has %d neighbours" % (es1, sum))
        if sum == 2:
            corners.append(es1)
    print(corners)
    return corners

def part1(input):
    tiles = parse_tiles(input)
    edges = compute_edges(tiles)
    corners = find_corners(edges)
    result = 1
    for corner in corners:
        result = result * corner
    return result

def part2(input):
    result = 0
    return result

def main():    

    # Official input
    input = read_inputfile("input20.txt")

    print("The solution for part 1 on the official input is %d" % (part1(input)))
    print("The solution for part 2 on the official input is %d" % (part2(input)))

if __name__ == "__main__": 
    main()

