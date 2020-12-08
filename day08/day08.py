#!/usr/bin/env python3

import re
import os
import sys

def execute_code(instructions):
    acc = 0
    i_ptr = 0
    already_run = []
    for i in range(0, len(instructions)):
        already_run.append(False)
    while i_ptr < len(instructions):
        (instr, arg) = instructions[i_ptr]
        if already_run[i_ptr]:
            return acc
        print("%s %d" % (instr, arg))
        already_run[i_ptr] = True
        if instr == "acc":
            acc += arg
        if instr == "jmp":
            i_ptr += arg
        else:
            i_ptr += 1
    return acc

def parse_instructions(input):
    instructions = []
    for line in input:
        (instr, arg_as_str) = line.split()
        arg = int(arg_as_str)
        instructions.append((instr, arg))
    return instructions

def compute08(input):
    instructions = parse_instructions(input)
    result = execute_code(instructions)
    return result

def compute08b(input):
    result = 0
    return result

def main():    

    # Official input
    input_file = os.path.abspath(os.path.dirname(__file__)) + os.path.sep + "input08.txt"
    with open(input_file) as f:
        input = [x.strip() for x in f]

    print("The solution for part 1 on the official input is %d" % (compute08(input)))
    print("The solution for part 2 on the official input is %d" % (compute08b(input)))

if __name__ == "__main__": 
    main()

