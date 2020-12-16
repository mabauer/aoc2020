#!/usr/bin/env python3

from enum import Enum
import re

from utils import read_inputfile
from itertools import permutations
from typing import Dict, List, Tuple

class Rules:

    def __init__(self):
        self.rules: Dict[str, List[Tuple[int, int]]] = {}

    def add(self, s):
        mo = re.search("([a-zA-Z ]+):\s([0-9]+)-([0-9]+)\sor\s([0-9]+)-([0-9]+)", s)
        if mo is not None:
            fieldname = mo.group(1)
            self.rules[fieldname] = []
            self.rules[fieldname].append((int(mo.group(2)), int(mo.group(3))))
            self.rules[fieldname].append((int(mo.group(4)), int(mo.group(5))))
            # print("%s: %s" % (fieldname, self.rules[fieldname]))

    def is_valid_wrt_any_rule(self, value: int) -> bool:
        for fieldname in self.rules:
            valid = self.is_valid_wrt_rule(fieldname, value)
            if valid == True:
                return True
        return False

    def is_valid_wrt_rule(self, fieldname, value):
        valid = False
        for (lower, upper) in self.rules[fieldname]:
            if value >= lower and value <= upper:
                valid = True
                break
        return valid


class Part(Enum):
    RULES = 1
    YOUR_TICKET = 2
    NEARBY_TICKETS = 3

def parse_input(input) -> Tuple[Rules, List[int], List[List[int]]]:
    rules = Rules()
    your_ticket : List[int]= []
    nearby_tickets : List[List[int]]= []
    part = Part.RULES
    for line in input:
        if line != "":
            if line == "your ticket:":
                part = Part.YOUR_TICKET
            elif line == "nearby tickets:":
                part = Part.NEARBY_TICKETS
            elif re.match("[0-9]+.*", line):
                line = line.replace(" ", "")
                tickets = [int(x) for x in line.split(",")]
                if part == Part.YOUR_TICKET:
                    your_ticket = tickets
                if part == Part.NEARBY_TICKETS:
                    nearby_tickets.append(tickets)
            else:
                rules.add(line)
    result = (rules, your_ticket, nearby_tickets)
    return result

def get_invalid_values(ticket: List[int], rules: Rules) -> List[int]:
    result = []
    for value in ticket:
        if not rules.is_valid_wrt_any_rule(value):
            result.append(value)
    return result


def part1(input):
    (rules, your_ticket, nearby_tickets) = parse_input(input)
    scanning_error = 0
    for ticket in nearby_tickets:
        invalid_values = get_invalid_values(ticket, rules)
        scanning_error += sum(invalid_values)
    return scanning_error

def find_match_naive(fields: List[str], possible_matches: Dict[str, List[int]], rules: Rules) -> List[str]:
    solution : List[str] = []
    for possible_solution in permutations(rules.rules.keys()):
        print
        i = 0
        solution_works = True
        # print(possible_solution)
        for fieldname in possible_solution:
            if i not in possible_matches[fieldname]:
                solution_works = False
                break
            i += 1
        if solution_works:
            solution = list(possible_solution)
            break
    return solution


def list_to_string(list: List[str]) -> str:
    return "".join(list)

def find_match(fields: List[str], possible_matches: Dict[str, List[int]], rules: Rules, 
        memo : Dict[str, List[str]] = None) -> List[str]: 
    if len(fields) == 1:
        if len(possible_matches)-1 in possible_matches[fields[0]]:
            print(fields[0])
            return fields
        else: 
            return []
    key = list_to_string(fields)
    if memo == None:
        memo = {}
    if memo is not None and key in memo:
        return memo[key]
    for fieldname in fields:
        position = len(possible_matches) - len(fields)
        if position in possible_matches[fieldname]:
            temp = fields.copy()
            temp.remove(fieldname)
            possible_solution = find_match(temp, possible_matches, rules, memo)
            if possible_solution != []:
                print(fieldname)
                result = [fieldname] + possible_solution
                if memo is not None:
                    memo[key] = result
                return result
    return []

def compute_your_ticket(rules, your_ticket_values, nearby_tickets) -> Dict[str, int]:
    possible_matches : Dict[str, List[int]] = {} 
    your_ticket : Dict[str, int] = {}
    for fieldname in rules.rules.keys():
        possible_matches[fieldname] = []
        for i in range(0, len(your_ticket_values)):
            is_valid = True
            for ticket in nearby_tickets:
                if not rules.is_valid_wrt_rule(fieldname, ticket[i]):
                    is_valid = False
                    break
            if is_valid:
                # print("position %d works for %s" % (i, fieldname))
                possible_matches[fieldname].append(i)
    # print(possible_matches)

    # solution = find_match_naive([field for field in rules.rules.keys()], possible_matches, rules)
    fields = [ field for field in rules.rules.keys() ]
    fields.sort(key=lambda field: len(possible_matches[field]))
    solution = find_match(fields, possible_matches, rules)
    print(solution)
    if solution is None or solution == []:
        raise ValueError("Could not assign fields properly!")
    i = 0
    for fieldname in solution:
        your_ticket[fieldname] = your_ticket_values[i]
        i += 1
    return your_ticket


def part2(input):
    (rules, your_ticket_values, nearby_tickets) = parse_input(input)

    # Remove invalid nearby tickets
    nearby_tickets_copy = nearby_tickets.copy()
    for ticket in nearby_tickets_copy:
        invalid_values = get_invalid_values(ticket, rules)
        if invalid_values != []:
            nearby_tickets.remove(ticket)

    # Compute the ticket
    your_ticket = compute_your_ticket(rules, your_ticket_values, nearby_tickets)

    # Multiply the values of all fields starting with "departure"
    result = 1
    for fieldname in your_ticket.keys():
        fst_word = fieldname.split(" ")[0]
        if fst_word is not None and fst_word == "departure": 
            result = result * your_ticket[fieldname] 
    return result


def main():    

    # Official input
    input = read_inputfile("input16.txt")

    print("The solution for part 1 on the official input is %d" % (part1(input)))
    print("The solution for part 2 on the official input is %d" % (part2(input)))

if __name__ == "__main__": 
    main()

