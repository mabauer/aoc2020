#!/usr/bin/env python3

import logging
import re
import os
import sys

from typing import List, Tuple

from utils import read_inputfile

def buses_in_service(s: str) -> List[int]:
    buses = s.split(",")
    return [ int(bus) for bus in buses if bus != "x"]

def find_next_bus(time: int, buses: List[int]) -> Tuple[int, int]:
    next_bus = 0
    t = time
    while next_bus == 0:
        for bus in buses:
            if t % bus == 0:
                next_bus = bus
                break
        t += 1
    return (next_bus, t-1)

def part1(input):
    time = int(input[0])
    buses = buses_in_service(input[1])
    (next_bus, departure_time) = find_next_bus(time, buses)
    result = (departure_time-time) * next_bus
    return result

def part2(s: str):
    buses = s.split(",")
    offsets: List[Tuple[int, int]] = []
    offset = 0
    highest_bus_number = 0
    offset_of_highest_bus = 0
    for bus in buses:
        if bus != "x":
            bus_number = int(bus)
            offsets.append((offset, bus_number))
            if (bus_number > highest_bus_number):
                offset_of_highest_bus = offset
                highest_bus_number = bus_number
        offset += 1  
    i = 1
    while True:
        time = i * highest_bus_number - offset_of_highest_bus 
        # print(time) 
        do_all_buses_match = True
        for (offset, bus_number) in offsets:
            if not (time + offset) % bus_number == 0:
                do_all_buses_match = False
                break
        if do_all_buses_match:
            return time
        i += 1
    
def main():    

    # Official input
    input = read_inputfile("input13.txt")

    print("The solution for part 1 on the official input is %d" % (part1(input)))
    print("The solution for part 2 on the official input is %d" % (part2(input[1])))

if __name__ == "__main__": 
    main()

