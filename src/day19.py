#!/usr/bin/env python3

import re
import os
import sys
from typing import Dict, List, Tuple

from utils import read_inputfile

Rules = Dict[int, List[List[int]]]
Patterns = Dict[int, List[str]]

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

def evaluate_rule(lhs : int, rules: Rules, patterns: Patterns) -> List[str]:
    if lhs in patterns:
        return patterns[lhs]
    result : List[str] = []
    for rhs in rules[lhs]:
        alts : List[str]= []
        for n in rhs:
            ps = evaluate_rule(n, rules, patterns)
            alts = append_patterns(alts, ps)
        result += alts
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
    patterns : Dict[int, List[str]] = {}
    for line in input:
        if re.match("(\d+): (\d+)", line):
            (lhs, rhs) = parse_rule(line)
            rules[lhs] = rhs
        mo = re.match("(\d+): \"([ab]+)\"", line)
        if mo is not None:
            patterns[int(mo.group(1))] = [mo.group(2)]
    return (rules, patterns)

def parse_messages(input) -> List[str]:
    result = []
    for line in input:
        if re.match("[ab]+", line):
            result.append(line)
    return result

def verify_messages(messages: List[str], valid_patterns: List[str]) -> int:
    result = 0
    for msg in messages:
        if msg in valid_patterns:
            result += 1
    return result


def part1(input):
    (rules, patterns) = parse_rules(input)
    print(rules)
    messages = parse_messages(input)
    patterns0 = evaluate_rule(0, rules, patterns)
    result = verify_messages(messages, patterns0)
    return result

def part2(input):
    result = 0
    return result

def main():    

    # Official input
    input = read_inputfile("input19.txt")

    print("The solution for part 1 on the official input is %d" % (part1(input)))
    print("The solution for part 2 on the official input is %d" % (part2(input)))

if __name__ == "__main__": 
    main()

