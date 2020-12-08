#!/usr/bin/env python3

import re
import os
import sys

def bisect(lower, upper):
    result = (lower + upper) // 2
    return result

# Compute a seat (row, col) from its code
def compute_seat(code):
    row = 0
    col = 0
    lower = 0
    upper = 127
    i = 0
    # Determine the row
    while i < 7:
        direction = code[i]
        if direction == "F":
            upper = bisect(lower, upper)
        if direction == "B":
            lower = bisect(lower, upper) + 1
        i = i + 1
    row = lower
    # Determine the column
    lower = 0
    upper = 7    
    while i < 10:
        direction = code[i]
        if direction == "L":
            upper = bisect(lower, upper)
        if direction == "R":
            lower = bisect(lower, upper) + 1
        i = i + 1
    col = lower
    return (row, col)

# Much better solution: treat code as binary numbers
def compute_seat2(code):
    code = code.replace("F", "0").replace("B", "1").replace("L", "0").replace("R", "1")
    print(code)
    row = int(code[0:7], 2)
    col = int(code[7:10], 2)
    return (row, col)

# Compute the seat id for a seat given by (row, col)
def compute_seatid(seat):
    (row, col) = seat
    return row * 8 + col

# Compute all seats
def compute_all_seatids(input):
    seats = []
    for line in input:
        seat = compute_seat(line)
        id = compute_seatid(seat)
        seats.append(id)
    return seats

# Find the highest seat id
def part1(input):
    seats = compute_all_seatids(input)
    return max(seats)

# Find our seat
def find_our_seat(seats):
    seats.sort()
    i = 1
    while i < len(seats):
        # Look for a gap in seat ids
        if seats[i] - seats[i-1] > 1 :
            # The gap is our seat!
            return seats[i-1] + 1
        i = i + 1
    return 0

def part2(input):
    seats = compute_all_seatids(input)
    return find_our_seat(seats)

# Print the cabin layout (including missing seats)
def print_cabin_layout(input):
    seats = compute_all_seatids(input)
    my_seat = find_our_seat(seats)
    i = 0
    for row in range(0, 128):
        print("%3d: " % row, end ='')
        for col in range(0,8):
            id = row*8 + col
            if id == my_seat:
                print("X ", end='')
            else:
                if id in seats:
                    print("# ", end='')
                else:
                    print(". ", end='')     
        print()
    print()

def main():    

    # Official input
    input_file = os.path.abspath(os.path.dirname(__file__)) + os.path.sep + "input05.txt"
    with open(input_file) as f:
        input = [x.strip() for x in f]

    print_cabin_layout(input)

    print("The solution for part 1 (highest seat id) is %d" % (part1(input)))
    print("The solution for part 2 (our seat id) is %d" % (part2(input)))

if __name__ == "__main__": 
    main()

