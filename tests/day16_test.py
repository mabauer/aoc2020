#!/usr/bin/env python3

import unittest
import os
import sys

from day16 import Rules, get_invalid_values, parse_input, part1, compute_your_ticket
from utils import read_inputfile

class Day16Test(unittest.TestCase):

    def test_parse_rules(self):
        input = ["class: 1-3 or 5-7", "row: 6-11 or 33-44", "seat: 13-40 or 45-50"]
        rules = Rules()
        for s in input:
            rules.add(s)

    def test_parse_input_on_example_data(self):
        input = read_inputfile("example16a.txt")
        (rules, your_ticket, nearby_tickets) = parse_input(input)
        self.assertEqual([k for k in rules.rules.keys()], ["class", "row", "seat"])
        self.assertEqual(your_ticket, [7,1,14])
        self.assertEqual(len(nearby_tickets), 4)

    def test_part1_on_example_data(self):
        input = read_inputfile("example16a.txt")
        self.assertEqual(part1(input), 71)

    def test_compute_your_ticket_on_example_data_b(self):
        input = read_inputfile("example16b.txt")
        (rules, your_ticket_values, nearby_tickets) = parse_input(input)
        nearby_tickets_copy = nearby_tickets.copy()
        for ticket in nearby_tickets_copy:
            invalid_values = get_invalid_values(ticket, rules)
            if invalid_values != []:
                nearby_tickets.remove(ticket)
        print("Valid nearby tickets: %s" % nearby_tickets)
        your_ticket = compute_your_ticket(rules, your_ticket_values, nearby_tickets)
        self.assertEqual(your_ticket["class"], 12)
        self.assertEqual(your_ticket["row"], 11)
        self.assertEqual(your_ticket["seat"], 13)

    def test_compute_your_ticket_on_example_data_a(self):
        input = read_inputfile("example16a.txt")
        (rules, your_ticket_values, nearby_tickets) = parse_input(input)
        nearby_tickets_copy = nearby_tickets.copy()
        for ticket in nearby_tickets_copy:
            invalid_values = get_invalid_values(ticket, rules)
            if invalid_values != []:
                nearby_tickets.remove(ticket)
        print("Valid nearby tickets: %s" % nearby_tickets)
        your_ticket = compute_your_ticket(rules, your_ticket_values, nearby_tickets)
        self.assertEqual(your_ticket["class"], 1)
        self.assertEqual(your_ticket["row"], 7)
        self.assertEqual(your_ticket["seat"], 14)


if __name__ == "__main__": 
    unittest.main()