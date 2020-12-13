#!/usr/bin/env python3

import logging
import re
import os
import sys

from typing import List, Tuple

from utils import read_inputfile

# Find all buses that are "in service"
def buses_in_service(s: str) -> List[int]:
    buses = s.split(",")
    return [ int(bus) for bus in buses if bus != "x"]

# Find the bus number of the earliest bus you can take to the airport, plus its departure time
# Returns a tuple (bus number, departure time)
def find_next_bus(time: int, buses: List[int]) -> Tuple[int, int]:
    next_bus = 0
    t = time
    while next_bus == 0:
        # Try if one of the buses in service starts departing at time t
        for bus in buses:
            if t % bus == 0:
                next_bus = bus
                break
        # If not, try one minute later
        t += 1
    return (next_bus, t-1)

# Find the bus number of the earliest bus you can take to the airport and multiply it 
# with its departure time
def part1(input):
    time = int(input[0])
    buses = buses_in_service(input[1])
    (next_bus, departure_time) = find_next_bus(time, buses)
    result = (departure_time-time) * next_bus
    return result


# Find the earliest timestamp such that the first bus number departs at that time 
# and each subsequent listed bus number departs at that subsequent minute.
def part2(s: str):
    buses = s.split(",")
    # Build pairs of (offset, bus_number)
    pairs: List[Tuple[int, int]] = []
    offset = 0
    for bus in buses:
        if bus != "x":
            bus_number = int(bus)
            pairs.append((offset, bus_number))
        offset += 1  
    # Solve the problem iteratively -- find a suitable solution for starting time for the first two buses,
    # Then use that solution to find one for an additional bus and so on...   
    # 1. Find i, where i * bus_number(0) + offset(1) % bus_number(1) == 0 
    #   => starting time suitable for buses 1 and 2 is i*bus_number(0)
    # 2. Find i, where i * bus_number(0)*bus_number(1) + offset(2) % bus_number(2) == 0
    #   => starting time suitbale for buses 1, 2 and 3 is previuos starting time + i*bus_number(0)*bus_number(1)
    # Continue until all buses are considered...
    (offset, bus_number) = pairs[0]
    time = 0   
    factor = bus_number 
    for (offset, bus_number) in pairs[1:]:
        # Try to find i such that i * bus_number(0) * .. * bus_number(n) + offset(n+1) %  busnumber(n+1) == 0
        i = 0
        while True:
            t = time + i*factor
            if (t + offset) % bus_number == 0:
                break
            i += 1
        # starting time = old start time + i * bus_number(0) * .. * bus_number(n)
        time = t
        # factor == product of all previuos bus_numbers
        factor = factor*bus_number
    return time

    
def main():    

    # Official input
    input = read_inputfile("input13.txt")

    print("The solution for part 1 on the official input is %d" % (part1(input)))
    print("The solution for part 2 on the official input is %d" % (part2(input[1])))

if __name__ == "__main__": 
    main()

