#!/usr/bin/env python3

import re
import os

from utils import read_inputfile

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

# Is this password a valid one according to the rules of part1?
def is_valid_passwd_part1(passwd, letter, min, max):
    count = count_occurences(passwd, letter)
    return (count >= min and count <= max)

# Is this password a valid one according to the rules of part2?
def is_valid_passwd_part2(passwd, letter, first, second):
    count = 0
    if passwd[first-1] == letter:
        count = count + 1
    if passwd[second-1] == letter:
        count = count + 1
    return (count == 1)

# Parse the input line
def is_valid_passwd_entry(line, is_valid_passwd_func):
    # "1-3 a: abcde"
    # (first)-(second) (letter): (passwd)
    mo = re.search("([0-9]+)\-([0-9]+)\s([a-zA-Z]):\s(.*)", line)
    first = int(mo.group(1))
    second = int(mo.group(2))
    letter = mo.group(3)
    passwd = mo.group(4)
    return is_valid_passwd_func(passwd, letter, first, second)

# Count the number of valid passwords
def count_valid_passwds(input, is_valid_password_func):
    result = 0
    for line in input:
        if is_valid_passwd_entry(line, is_valid_password_func):
            # print("%s -- valid" % (line))
            result = result + 1
        # else:
        #   print("%s -- invalid" % (line))
    return result

def main():

    input = read_inputfile("input02.txt")

    print("According to part1, the input contains %d valid passwords" 
        % count_valid_passwds(input, is_valid_passwd_part1))
    print("According to part2, the input contains %d valid passwords" 
        % count_valid_passwds(input, is_valid_passwd_part2))

if __name__ == "__main__": 
    main()
