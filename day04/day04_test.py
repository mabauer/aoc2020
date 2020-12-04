#!/usr/bin/env python3

import unittest
import os
import sys

import day04

class Day04Test(unittest.TestCase):

    def test_field_validations(self):
        self.assertTrue(day04.is_valid_year("2002", 1920, 2002))
        self.assertFalse(day04.is_valid_year("2003", 1920, 2002))

        self.assertTrue(day04.is_valid_hgt("60in"))
        self.assertTrue(day04.is_valid_hgt("190cm"))
        self.assertFalse(day04.is_valid_hgt("190"))

        self.assertTrue(day04.is_valid_hcl("#123abc"))
        self.assertFalse(day04.is_valid_hcl("#123abz"))
        self.assertFalse(day04.is_valid_hcl("123abc"))

        self.assertTrue(day04.is_valid_ecl("brn"))
        self.assertFalse(day04.is_valid_ecl("wat"))

        self.assertTrue(day04.is_valid_pid("000000001"))
        self.assertFalse(day04.is_valid_pid("0123456789"))

    def test_part1_on_example_data(self):
        input_file = os.path.abspath(os.path.dirname(__file__)) + os.path.sep + "example04.txt"
        with open(input_file) as f:
            input = [x.strip() for x in f]
        self.assertEqual(day04.count_passports(input, True), 2)

    def test_part2_valid_passports(self):
        input = [
            "pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980",
            "hcl:#623a2f",
            "",
            "eyr:2029 ecl:blu cid:129 byr:1989",
            "iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm",
            "",
            "hcl:#888785",
            "hgt:164cm byr:2001 iyr:2015 cid:88",
            "pid:545766238 ecl:hzl",
            "eyr:2022",
            "",
            "iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719"]
        self.assertEqual(day04.count_passports(input, False), 4)

    def test_part2_invalid_passports(self):
        input = [
            "eyr:1972 cid:100"
            "hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926"
            ""
            "iyr:2019"
            "hcl:#602927 eyr:1967 hgt:170cm"
            "ecl:grn pid:012533040 byr:1946"
            ""
            "hcl:dab227 iyr:2012"
            "ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277"
            ""
            "hgt:59cm ecl:zzz"
            "eyr:2038 hcl:74454a iyr:2023"
            "pid:3556412378 byr:2007"]
        self.assertEqual(day04.count_passports(input, False), 0)    

if __name__ == "__main__": 
    unittest.main()