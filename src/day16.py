#!/usr/bin/env python3

from enum import Enum
import re

from utils import read_inputfile
from itertools import permutations
from typing import Dict, List, Tuple

Ticket = List[int]

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

    def is_valid_wrt_rule(self, fieldname, value):
        valid = False
        for (lower, upper) in self.rules[fieldname]:
            if value >= lower and value <= upper:
                valid = True
                break
        return valid

    def is_valid_wrt_any_rule(self, value: int) -> bool:
        for fieldname in self.rules:
            valid = self.is_valid_wrt_rule(fieldname, value)
            if valid == True:
                return True
        return False

    def get_invalid_values(self, ticket: Ticket) -> List[int]:
        result = []
        for value in ticket:
            if not self.is_valid_wrt_any_rule(value):
                result.append(value)
        return result

    def get_valid_tickets(self, tickets: List[Ticket]) -> List[Ticket]:
        result : List[Ticket] = []
        for ticket in tickets:
            invalid_values = self.get_invalid_values(ticket)
            if invalid_values == []:
                result.append(ticket)
        return result

class Part(Enum):
    RULES = 1
    YOUR_TICKET = 2
    NEARBY_TICKETS = 3

def parse_input(input) -> Tuple[Rules, Ticket, List[Ticket]]:
    rules = Rules()
    your_ticket : Ticket = []
    nearby_tickets : List[Ticket]= []
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


def part1(input):
    (rules, your_ticket, nearby_tickets) = parse_input(input)
    scanning_error = 0
    for ticket in nearby_tickets:
        invalid_values = rules.get_invalid_values(ticket)
        scanning_error += sum(invalid_values)
    return scanning_error


def find_mapping_naive(fields: List[str], possible_positions: Dict[str, List[int]], rules: Rules) -> List[str]:
    mapping : List[str] = []
    for possible_mapping in permutations(rules.rules.keys()):
        print
        i = 0
        mapping_works = True
        # print(possible_mapping)
        for fieldname in possible_mapping:
            if i not in possible_positions[fieldname]:
                mapping_works = False
                break
            i += 1
        if mapping_works:
            mapping = list(possible_mapping)
            break
    return mapping

def list_to_string(list: List[str]) -> str:
    return "".join(list)

def find_mapping(fields: List[str], possible_positions: Dict[str, List[int]], rules: Rules, 
        memo : Dict[str, List[str]] = None) -> List[str]: 
    if len(fields) == 1:
        if len(possible_positions)-1 in possible_positions[fields[0]]:
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
        position = len(possible_positions) - len(fields)
        if position in possible_positions[fieldname]:
            temp = fields.copy()
            temp.remove(fieldname)
            possible_mapping = find_mapping(temp, possible_positions, rules, memo)
            if possible_mapping != []:
                # print(fieldname)
                result = [fieldname] + possible_mapping
                if memo is not None:
                    memo[key] = result
                return result
    return []

def compute_our_ticket(rules : Rules, our_ticket : Ticket, nearby_tickets) -> Dict[str, int]:
    possible_positions : Dict[str, List[int]] = {} 
    result : Dict[str, int] = {}
    # For each rule compute all possibly valid ticket positions when all nearby tickets are considered  
    for fieldname in rules.rules.keys():
        possible_positions[fieldname] = []
        for i in range(0, len(our_ticket)):
            is_valid = True
            for ticket in nearby_tickets:
                if not rules.is_valid_wrt_rule(fieldname, ticket[i]):
                    is_valid = False
                    break
            if is_valid:
                # print("position %d works for %s" % (i, fieldname))
                possible_positions[fieldname].append(i)
    # print(possible_positions)

    # Find a correct mapping of fieldnames to ticket positions
    # mapping = find_mapping_naive([field for field in rules.rules.keys()], possible_positions, rules)
    fields = [ field for field in rules.rules.keys() ]
    fields.sort(key=lambda field: len(possible_positions[field]))
    mapping = find_mapping(fields, possible_positions, rules)
    # print(mapping)
    if mapping is None or mapping == []:
        raise ValueError("Could not assign fields properly!")

    # Use the mapping to assign values to our tickez
    i = 0
    for fieldname in mapping:
        result[fieldname] = our_ticket[i]
        i += 1
    return result


def part2(input):
    (rules, our_ticket_values, nearby_tickets) = parse_input(input)

    # Remove invalid nearby tickets
    nearby_tickets = rules.get_valid_tickets(nearby_tickets)

    # Compute the ticket
    our_ticket = compute_our_ticket(rules, our_ticket_values, nearby_tickets)

    # Multiply the values of all fields starting with "departure"
    result = 1
    for fieldname in our_ticket.keys():
        fst_word = fieldname.split(" ")[0]
        if fst_word is not None and fst_word == "departure": 
            result = result * our_ticket[fieldname] 
    return result


def main():    

    # Official input
    input = read_inputfile("input16.txt")

    print("The solution for part 1 on the official input is %d" % (part1(input)))
    print("The solution for part 2 on the official input is %d" % (part2(input)))

if __name__ == "__main__": 
    main()

