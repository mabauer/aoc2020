#!/usr/bin/env python3

import os

from utils import read_inputfile

# Find two integers in a list that sum up to 2020
def find_two_entries_for_2020(expenses):
    i = 0
    while i < len(expenses):
        j = i + 1
        while j < len(expenses):
            if (expenses[i] + expenses[j] == 2020):
                return (expenses[i], expenses[j])
            j = j + 1
        i = i + 1

# Find three integers in a list that sum up to 2020
def find_three_entries_for_2020(expenses):
    for first in expenses:
        for second in expenses:
            for third in expenses:
                if first != second and first != third and second != third: 
                    if (first + second + third) == 2020:
                        return (first, second, third)


def main():

    input = [ int(s) for s in read_inputfile("input01.txt") ]

    (first, second) = find_two_entries_for_2020(input)
    print("The answer for part one is: %d" % (first*second))

    (first, second, third) = find_three_entries_for_2020(input)
    print("The answer on official data is: %d" % (first*second*third))

if __name__ == "__main__": 
    main()

