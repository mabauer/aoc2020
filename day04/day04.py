#!/usr/bin/env python3

import re

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

# Count valid passports
def count_passports(input, skip_partii_checks):
    count = 0
    passport = {}
    for line in input:
        # Empty line: new passport values starts, we can validate the old ones
        if line == "":
            # print(passport)
            if is_passport_valid(passport, skip_partii_checks):
                count = count + 1
            passport = {}
        items = line.split()
        for item in items:
            # item conforms to "key:value"
            key_value = item.split(":")
            passport[key_value[0]] = key_value[1]
    # Don't forget the last one if the input does not end with an empty line
    if line != "":
        if is_passport_valid(passport, skip_partii_checks):
            count = count + 1
    return count

def run_tests():
    assert is_valid_year("2002", 1920, 2002)
    assert not is_valid_year("2003", 1920, 2002)

    assert is_valid_hgt("60in")
    assert is_valid_hgt("190cm")
    assert not is_valid_hgt("190")
    
    assert is_valid_hcl("#123abc")
    assert not is_valid_hcl("#123abz")
    assert not is_valid_hcl("123abc")
    
    assert is_valid_ecl("brn")
    assert not is_valid_ecl("wat")

    assert is_valid_pid("000000001")
    assert not is_valid_pid("0123456789")

run_tests()

# Example data
with open("example04.txt") as f:
    input1 = [x.strip() for x in f]

# Official input
with open("input04.txt") as f:
    input2 = [x.strip() for x in f]

print("The solution for part 1 on the example data is %d" % (count_passports(input1, True)))
print("The solution for part 1 on the official input is %d" % (count_passports(input2, True)))

print("The solution for part 2 on the example data is %d" % (count_passports(input1, False)))
print("The solution for part 2 on the official data is %d" % (count_passports(input2, False)))


