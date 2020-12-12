#!/usr/bin/env python3

import re
import os

from utils import read_inputfile

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

# Count the number of valid passwords
def count_valid_passwds(input):
    result = 0
    for line in input:
        if is_valid_passwd_entry(line):
            # print("%s -- valid" % (line))
            result = result + 1
        # else:
        #   print("%s -- invalid" % (line))
    return result

def main():
    # Example data
    input1 = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]

    print("The example data has %d valid passwords" % (count_valid_passwds(input1)))

    # Official data
    input2 = read_inputfile("input02.txt")

    print("The official data has %d valid passwords" % (count_valid_passwds(input2)))

if __name__ == "__main__": 
    main()
