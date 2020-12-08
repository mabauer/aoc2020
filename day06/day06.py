#!/usr/bin/env python3

import re
import os
import sys

class Group:

    def __init__(self): 
        self.number_of_persons = 0
        # Dictionary: answer -> counter, how often this answer was given
        self.answers = {}

    # Adds a new person with their answers (e.g. "abcx")
    def add_person(self, answers):
        self.number_of_persons += 1
        i = 0
        while i < len(answers):
            answer = answers[i]
            if answer >= 'a' and answer <='z':
                self.add_answer(answer)
            i = i + 1

    def add_answer(self, answer):
        if answer in self.answers:
            self.answers[answer] += 1
        else:
            self.answers[answer] = 1

    # Return a list of answers that are given by *anyone*
    def answers_by_anyone(self):
        return self.answers.keys()

    # Return a list of answers that are given by *everyone*
    def answers_by_everyone(self):
        result = [];
        for answer in self.answers.keys():
            if self.answers[answer] == self.number_of_persons:
                result.append(answer)
        return result

    # For debugging
    def __repr__(self):
        str = "({persons}) {answers}" 
        return str.format(persons=self.number_of_persons, answers=self.answers)

def parse_groups(input):
    groups = []
    group = Group()
    for line in input:
        if line == "":
            # Empy line => new group
            groups.append(group)
            group = Group()
        else:
            # => new person
            group.add_person(line)
    if line != "":
        groups.append(group)
    return groups 

# Count the questions to which anyone in a group answered with "yes"
def part1(input):
    groups = parse_groups(input)
    # print(groups)
    sum = 0
    for group in groups:
        sum = sum + len(group.answers_by_anyone())
    return sum

# Count the questions to which everyone in a group answered with "yes"
def part2(input):
    groups = parse_groups(input)
    # print(groups)
    sum = 0
    for group in groups:
        sum = sum + len(group.answers_by_everyone())
    return sum

def main():    

    # Official input
    input_file = os.path.abspath(os.path.dirname(__file__)) + os.path.sep + "input06.txt"
    with open(input_file) as f:
        input = [x.strip() for x in f]

    print("The solution for part 1 on the official input is %d" % (part1(input)))
    print("The solution for part 2 on the official input is %d" % (part2(input)))

if __name__ == "__main__": 
    main()

