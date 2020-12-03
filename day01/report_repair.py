#!/usr/bin/env python3

# Find two integers in a list that sum up to 2020
def find_entries_for_2020(expenses):
    i = 0
    while i < len(expenses):
        j = i + 1
        while j < len(expenses):
            if (expenses[i] + expenses[j] == 2020):
                return (expenses[i], expenses[j])
            j = j + 1
        i = i + 1

# Example data
input1 = [1721, 979, 366, 299, 675, 1456]
(first, second) = find_entries_for_2020(input1)
print("The example result is %d * %d = %d" % (first, second, first*second))

# Official data
with open("input01.txt") as f:
    input2 = [int(x) for x in f]

(first, second) = find_entries_for_2020(input2)
print("The answer on official data is: %d" % (first*second))


