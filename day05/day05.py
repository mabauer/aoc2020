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

# Compute the seat id for a seat given by (row, col)
def compute_seatid(seat):
    (row, col) = seat
    return row * 8 + col

# Find the highest seat id
def compute05(input):
    max = 0
    for line in input:
        seat = compute_seat(line)
        id = compute_seatid(seat)
        if id > max:
            max = id
    return max

# Find our seat
def compute05b(input):
    seats = []
    for line in input:
        seat = compute_seat(line)
        id = compute_seatid(seat)
        seats.append(id)

    seats.sort()
    i = 1
    while i < len(seats):
        # Look for a gap in seat ids
        if seats[i] - seats[i-1] > 1 :
            # The gap is our seat!
            return seats[i-1] + 1
        i = i + 1
    return 0

def main():    

    # Official input
    input_file = os.path.abspath(os.path.dirname(__file__)) + os.path.sep + "input05.txt"
    with open(input_file) as f:
        input = [x.strip() for x in f]

    print("The solution for part 1 (highest seat id) is %d" % (compute05(input)))
    print("The solution for part 2 (our seat id) is %d" % (compute05b(input)))

if __name__ == "__main__": 
    main()

