#!/usr/bin/env python3

import re

# Count the number of occurences of str2 in str1
def count_occurences(str1, str2):
    pos = 0
    count = 0
    while pos >= 0:
        pos = str1.find(str2)
        if pos >= 0:
            count = count + 1
            str1 = str1[pos + len(str2):]
    return count

# Is this password a valid one?
def is_valid_passwd(passwd, letter, min, max):
    count = count_occurences(passwd, letter)
    return (count >= min and count <= max)

# Parse the input line
def is_valid_passwd_entry(line):
    # "1-3 a: abcde"
    # (min)-(max) (letter): (passwd)
    mo = re.search("([0-9]+)\-([0-9]+)\s([a-zA-Z]):\s(.*)", line)
    min = int(mo.group(1))
    max = int(mo.group(2))
    letter = mo.group(3)
    passwd = mo.group(4)
    return is_valid_passwd(passwd, letter, min, max)
            
# Example
input1 = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]

result = 0
for line in input1:
    if is_valid_passwd_entry(line):
        print("%s -- valid" % (line))
        result = result + 1
    else:
        print("%s -- invalid" % (line))
print("The example has %d valid passwords" % (result))

# Solution
with open("input02.txt") as f:
    input2 = [x.strip() for x in f]

result = 0
for line in input2:
    if is_valid_passwd_entry(line):
        print("%s -- valid" % (line))
        result = result + 1
    else:
        print("%s -- invalid" % (line))
print("The input has %d valid passwords" % (result))
