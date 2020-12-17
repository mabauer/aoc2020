#!/usr/bin/env python3

from typing import Dict, List, Tuple

from utils import read_inputfile

ACTIVE = "#"
INACTIVE = "."

# 3D "Game of Life"
class Game3D:

    def __init__(self, lines: List[str]):
        self.cells : Dict[Tuple[int, int, int], str] = {}
        width = len(lines[0])
        height = len(lines)
        self.x_min = 0 - (width // 2)
        self.x_max = self.x_min + width - 1
        self.y_min = 0 - (height // 2)
        self.y_max = self.y_min + height - 1
        self.z_max = 0
        self.z_min = 0
        for y in range(self.y_min, self.y_max + 1):
            for x in range(self.x_min, self.x_max + 1):
                self.set_cell(x, y, 0, lines[-self.y_min+y][-self.x_min+x])
            print()

    
    # Compute a new generation according to the rules of part 1
    # Returns True, if thee new generation differs from the old one.
    def next_generation(self) -> bool:

        # Expand game area
        self.z_min -= 1
        self.z_max += 1
        self.y_min -= 1
        self.y_max += 1
        self.x_min -= 1
        self.x_max += 1

        # Precalculate the number of neighbours
        number_of_neighbours : Dict[Tuple[int, int, int], int] = {}
        for z in range(self.z_min, self.z_max + 1):
            for y in range(self.y_min, self.y_max + 1):
                for x in range(self.x_min, self.x_max + 1):
                    number_of_neighbours[(x, y, z)] = self.count_active_neighbours(x, y, z)

        # Compute next generation
        changed = False
        for z in range(self.z_min, self.z_max + 1):
            for y in range(self.y_min, self.y_max + 1):
                for x in range(self.x_min, self.x_max + 1):
                    old_state = self.get_cell(x, y, z)
                    c = number_of_neighbours[(x, y, z)]
                    # print(c, end="")
                    if old_state == INACTIVE and (c == 3):
                        self.set_cell(x, y, z, ACTIVE)
                    if old_state == ACTIVE and (c != 2 and c != 3):
                        self.set_cell(x, y, z, INACTIVE)
                    if self.get_cell(x, y, z) != old_state:
                        changed = True 
                # print()
            # print()
        return changed

    def get_cell(self, x: int, y: int, z: int)  -> str:
        if x < self.x_min and x > self.x_max:
            return INACTIVE
        if y < self.y_min and y > self.y_max:
            return INACTIVE
        if z < self.z_min and z > self.z_max:
            return INACTIVE
        if (x, y, z) in self.cells:
            return self.cells[(x, y, z)]
        else:
            return INACTIVE

    def set_cell(self, x: int, y: int, z: int, value: str):
        if x < self.x_min and x > self.x_max:
            raise ValueError("x coordinate out of range")
        if y < self.y_min and y > self.y_max:
            raise ValueError("y coordinate out of range")
        if z < self.z_min and z > self.z_max:
            raise ValueError("z coordinate out of range")
        self.cells[(x, y, z)] = value

    # Count the number of occupied cells next to the cell (x, y)
    def count_active_neighbours(self, x: int, y: int, z: int) -> int:
        result = 0
        for z1 in range(z-1, z+2):
            for y1 in range(y-1, y+2):
                for x1 in range(x-1, x+2):
                    if self.get_cell(x1, y1, z1) == ACTIVE:
                        result += 1
        if self.get_cell(x, y, z) == ACTIVE:
            result -= 1
        return result

    # Count the occupied seats in the game
    def count_active_cells(self):
        result = 0
        for cell in self.cells:
            if self.cells[cell] == ACTIVE:
                result += 1
        return result

    def print(self):
        for z in range(self.z_min, self.z_max + 1):
            print("z=%d" % z)
            for y in range(self.y_min, self.y_max + 1):
                for x in range(self.x_min, self.x_max + 1):
                    print(self.get_cell(x, y, z), end="")
                print()
            print()


class Game4D:

    def __init__(self, lines: List[str]):
        self.cells : Dict[Tuple[int, int, int, int], str] = {}
        width = len(lines[0])
        height = len(lines)
        self.x_min = 0 - (width // 2)
        self.x_max = self.x_min + width - 1
        self.y_min = 0 - (height // 2)
        self.y_max = self.y_min + height - 1
        self.z_min = 0
        self.z_max = 0
        self.w_min = 0
        self.w_max = 0
        for y in range(self.y_min, self.y_max + 1):
            for x in range(self.x_min, self.x_max + 1):
                self.set_cell(x, y, 0, 0, lines[-self.y_min+y][-self.x_min+x])
            print()

    
    # Compute a new generation according to the rules of part 1
    # Returns True, if thee new generation differs from the old one.
    def next_generation(self) -> bool:

        # Expand game area
        self.z_min -= 1
        self.z_max += 1
        self.y_min -= 1
        self.y_max += 1
        self.x_min -= 1
        self.x_max += 1
        self.w_min -= 1
        self.w_max += 1

        # Precalculate the number of neighbours
        number_of_neighbours : Dict[Tuple[int, int, int, int], int] = {}
        for w in range(self.w_min, self.w_max +1 ):
            for z in range(self.z_min, self.z_max + 1):
                for y in range(self.y_min, self.y_max + 1):
                    for x in range(self.x_min, self.x_max + 1):
                        number_of_neighbours[(x, y, z, w)] = self.count_active_neighbours(x, y, z, w)

        # Compute next generation
        changed = False
        for w in range(self.w_min, self.w_max + 1):
            for z in range(self.z_min, self.z_max + 1):
                for y in range(self.y_min, self.y_max + 1):
                    for x in range(self.x_min, self.x_max + 1):
                        old_state = self.get_cell(x, y, z, w)
                        c = number_of_neighbours[(x, y, z, w)]
                        if old_state == INACTIVE and (c == 3):
                            self.set_cell(x, y, z, w, ACTIVE)
                        if old_state == ACTIVE and (c != 2 and c != 3):
                            self.set_cell(x, y, z, w, INACTIVE)
                        if self.get_cell(x, y, z) != old_state:
                            changed = True 
        return changed

    def get_cell(self, x: int, y: int, z: int, w: int = 0)  -> str:
        if x < self.x_min and x > self.x_max:
            return INACTIVE
        if y < self.y_min and y > self.y_max:
            return INACTIVE
        if z < self.z_min and z > self.z_max:
            return INACTIVE
        if w < self.w_min and z > self.w_max:
            return INACTIVE
        if (x, y, z, w) in self.cells:
            return self.cells[(x, y, z, w)]
        else:
            return INACTIVE

    def set_cell(self, x: int, y: int, z: int, w: int, value: str):
        if x < self.x_min and x > self.x_max:
            raise ValueError("x coordinate out of range")
        if y < self.y_min and y > self.y_max:
            raise ValueError("y coordinate out of range")
        if z < self.z_min and z > self.z_max:
            raise ValueError("z coordinate out of range")
        if w < self.w_min and z > self.w_max:
            raise ValueError("w coordinate out of range")
        self.cells[(x, y, z, w)] = value

    # Count the number of occupied cells next to the cell (x, y)
    def count_active_neighbours(self, x: int, y: int, z: int, w: int) -> int:
        result = 0
        for w1 in range(w-1, w+2):
            for z1 in range(z-1, z+2):
                for y1 in range(y-1, y+2):
                    for x1 in range(x-1, x+2):
                        if self.get_cell(x1, y1, z1, w1) == ACTIVE:
                            result += 1
        if self.get_cell(x, y, z, w) == ACTIVE:
            result -= 1
        return result

    # Count the occupied seats in the game
    def count_active_cells(self):
        result = 0
        for cell in self.cells:
            if self.cells[cell] == ACTIVE:
                result += 1
        return result

    def print(self):
        for w in range(self.w_min, self.w_max + 1):
            for z in range(self.z_min, self.z_max + 1):
                print("z=%d, w=%d" % (z, w))
                for y in range(self.y_min, self.y_max + 1):
                    for x in range(self.x_min, self.x_max + 1):
                        print(self.get_cell(x, y, z), end="")
                    print()
                print()


def part1(input, max_gens = 6):
    game = Game3D(input)
    gens = 0
    game.print()
    is_stable = False
    while gens < max_gens:
        gens += 1
        is_stable = not game.next_generation()
        game.print()
        print("Active: %d" % game.count_active_cells())
        if is_stable:
            break
    if is_stable:
        print("Stable after %d generations." % gens)
    result = game.count_active_cells()
    return result


def part2(input, max_gens = 6):
    game = Game4D(input)
    gens = 0
    game.print()
    is_stable = False
    while gens < max_gens:
        gens += 1
        is_stable = not game.next_generation()
        game.print()
        print("Active: %d" % game.count_active_cells())
        if is_stable:
            break
    if is_stable:
        print("Stable after %d generations." % gens)
    result = game.count_active_cells()
    return result

def main():    

    # Official input
    input = read_inputfile("input17.txt")

    print("The solution for part 1 on the official input is %d" % (part1(input)))
    print("The solution for part 2 on the official input is %d" % (part2(input)))

if __name__ == "__main__": 
    main()
