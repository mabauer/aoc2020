#!/usr/bin/env python3

import re
import os
import sys

# Is year based field valid (within min..max)?
def is_valid_year(year, min, max):
    if len(year) != 4:
        return false
    try:
        value = int(year)
        if value < min or value > max:
            return False
        return True
    except ValueError:
        return False

# Is height field valid (for inches and cms)?
def is_valid_hgt(s):
    hgt = s[:(len(s)-2)] 
    unit = s[(len(s)-2):]
    if unit != "cm" and unit != "in":
        return False
    try:
        value = int(hgt)
        if unit == "cm" and (value < 150 or value > 193):
            return False
        if unit == "in" and (value < 59 or value > 76):
            return False
        return True
    except ValueError:
        return False

# Alternative implementation using regex
def is_valid_hgt2(s):
    mo = re.search("(\d+)(in|cm)", s)
    if not mo:
        return False
    hgt = mo.group(1) 
    unit = mo.group(2)
    try:
        value = int(hgt)
        if unit == "cm" and (value < 150 or value > 193):
            return False
        if unit == "in" and (value < 59 or value > 76):
            return False
        return True
    except ValueError:
        return False    

# Is hair color valid (6 digit hex code)?
def is_valid_hcl(s):
    if len(s) != 7:
        return False
    if s[0] != "#":
        return False
    try:
        value = int(s[1:], 16)
        return True
    except ValueError:
        return False  

# Is eye color valid (predefined values)?
def is_valid_ecl(s):
    valid_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    return (s in valid_colors) 

# Is passport ID valid (9 digit number with leading 0s)
def is_valid_pid(s):
    if len(s) != 9:
        return False
    try:
        value = int(s)
        return True
    except ValueError:
        return False 

# Is passport valid -- if skip_partii_checks == true, skip detailed validation on fields
def is_passport_valid(passport, skip_partii_checks=True):
    mandatory_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    for field in mandatory_fields:
        if field not in passport:
            return False
    if skip_partii_checks:
        return True
    return (is_valid_year(passport["byr"], 1920, 2002) 
        and is_valid_year(passport["iyr"], 2010, 2020) 
        and is_valid_year(passport["eyr"], 2020, 2030)
        and is_valid_hgt(passport["hgt"])
        and is_valid_hcl(passport["hcl"])
        and is_valid_ecl(passport["ecl"])
        and is_valid_pid(passport["pid"]))

# Parse passports into a list of passports, each passport is represented as a dictionary
def parse_passports(input):
    passports = []
    passport = {}
    for line in input:
        # Empty line: new passport values starts, we can validate the old ones
        if line == "": 
            passports.append(passport)
            passport = {}
        items = line.split()
        for item in items:
            # item conforms to "key:value"
            key_value = item.split(":")
            passport[key_value[0]] = key_value[1]
    # Don't forget the last one if the input does not end with an empty line
    if line != "":
        passports.append(passport)
    return passports

# Count valid passports
def count_passports(input, skip_partii_checks):
    count = 0
    passports = parse_passports(input)
    for passport in passports:
        if is_passport_valid(passport, skip_partii_checks):
            count = count + 1
    return count

def main():    

    # Official input
    input_file = os.path.abspath(os.path.dirname(__file__)) + os.path.sep + "input04.txt"
    with open(input_file) as f:
        input = [x.strip() for x in f]

    print("The solution for part 1 on the official input is %d" % (count_passports(input, True)))
    print("The solution for part 2 on the official input is %d" % (count_passports(input, False)))

if __name__ == "__main__": 
    main()

