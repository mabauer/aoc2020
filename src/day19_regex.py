#!/usr/bin/env python3

import re
import os
import sys
from typing import Dict, List, Tuple

from utils import read_inputfile

Rules = Dict[int, List[List[int]]]
Patterns = Dict[int, str]

def append_patterns(list1: List[str], list2: List[str]) -> List[str]:
    result = []
    if list1 == []:
        return [e2 for e2 in list2]
    if list2 == []:
        return [e1 for e1 in list1]
    for e1 in list1:
        for e2 in list2:
            result.append(e1+e2)
    return result

def evaluate_rule(lhs : int, rules: Rules, patterns: Patterns) -> str:
    if lhs in patterns:
        return patterns[lhs]
    alternatives : List[str] = []
    for alt in rules[lhs]:
        ps = ""
        for n in alt:
            p = evaluate_rule(n, rules, patterns)
            ps = ps + p
        ps = "(" + ps + ")"
        # print(ps)
        alternatives.append(ps)
    result = "(" + "|".join(alternatives) + ")"
    patterns[lhs] = result
    return result


def parse_rule(line: str) -> Tuple[int, List[List[int]]]:
    tokens = line.split(" ")
    lhs = int(tokens[0].replace(":", ""))
    alternatives = []
    rhs : List[int]= []
    for token in tokens[1:]:
        if token == "|":
            alternatives.append(rhs)
            rhs = []
        else:
            rhs.append(int(token))
    alternatives.append(rhs)
    return (lhs, alternatives)    

def parse_rules(input) -> Tuple[Rules, Patterns]:
    rules : Dict[int, List[List[int]]] = {}
    patterns : Dict[int, str] = {}
    for line in input:
        if re.match("(\d+): (\d+)", line):
            (lhs, rhs) = parse_rule(line)
            rules[lhs] = rhs
        mo = re.match("(\d+): \"([ab]+)\"", line)
        if mo is not None:
            patterns[int(mo.group(1))] = mo.group(2)
    return (rules, patterns)

def parse_messages(input) -> List[str]:
    result = []
    for line in input:
        if re.match("[ab]+", line):
            result.append(line)
    return result

def verify_messages(messages: List[str], pattern: str) -> int:
    result = 0
    for msg in messages:
        if re.fullmatch(pattern, msg):
            print("Verified: %s" %msg)
            result += 1
    return result


def part1(input):
    (rules, patterns) = parse_rules(input)
    messages = parse_messages(input)
    pattern = evaluate_rule(0, rules, patterns)
    result = verify_messages(messages, pattern)
    return result

def part2(input):
    (rules, patterns) = parse_rules(input)
    messages = parse_messages(input)

    rules[8] = [ [ 42 ]*i for i in range(1, 10) ]
    rules[11] = [ [ 42]*i + [31]*i for i in range(1, 10) ]

    pattern = evaluate_rule(0, rules, patterns)

    result = verify_messages(messages, pattern)
    return result

def main():    

    # Official input
    input = read_inputfile("input19.txt")

    print("The solution for part 1 on the official input is %d" % (part1(input)))
    print("The solution for part 2 on the official input is %d" % (part2(input)))

if __name__ == "__main__": 
    main()

