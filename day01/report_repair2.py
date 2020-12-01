#!/usr/bin/env python3

# Find three integers in a list that sum up to 2020
def find_entries_for_2020(expenses):
    for first in expenses:
        for second in expenses:
            for third in expenses:
                if first != second and first != third and second != third: 
                    if (first + second + third) == 2020:
                        return (first, second, third)

# Example 
input1 = [1721, 979, 366, 299, 675, 1456]
(first, second, third) = find_entries_for_2020(input1)
print("The example result is %d * %d * %d = %d" % (first, second, third, first*second*third))

# Solution 
with open("input01.txt") as f:
    input2 = [int(x) for x in f]

(first, second, third) = find_entries_for_2020(input2)
print("The answer is: %d" % (first*second*third))


