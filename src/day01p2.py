#!/usr/bin/env python3

import os

from utils import read_inputfile

# Find three integers in a list that sum up to 2020
def find_entries_for_2020(expenses):
    for first in expenses:
        for second in expenses:
            for third in expenses:
                if first != second and first != third and second != third: 
                    if (first + second + third) == 2020:
                        return (first, second, third)

def main(): 
    # Example data
    input1 = [1721, 979, 366, 299, 675, 1456]
    (first, second, third) = find_entries_for_2020(input1)
    print("The example result is %d * %d * %d = %d" % (first, second, third, first*second*third))

    # Official data 
    input2 = [ int(s) for s in read_inputfile("input01.txt") ]

    (first, second, third) = find_entries_for_2020(input2)
    print("The answer on official data is: %d" % (first*second*third))

if __name__ == "__main__": 
    main()

