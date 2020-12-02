#!/usr/bin/env python3

import re

# Is this password a valid one?
def is_valid_passwd(passwd, letter, first, second):
    count = 0
    if passwd[first-1] == letter:
        count = count + 1
    if passwd[second-1] == letter:
        count = count + 1
    return (count == 1)

# Parse the input line
def is_valid_passwd_entry(line):
    # "1-3 a: abcde"
    # (first)-(second) (letter): (passwd)
    mo = re.search("([0-9]+)\-([0-9]+)\s([a-zA-Z]):\s(.*)", line)
    first = int(mo.group(1))
    second = int(mo.group(2))
    letter = mo.group(3)
    passwd = mo.group(4)
    return is_valid_passwd(passwd, letter, first, second)
            
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



