#!/usr/bin/env python3

import re
import os
import sys

from typing import List
from typing import Tuple

from utils import read_inputfile

Instruction = Tuple[str, int]

# Parse program code into a list of instruction tuples (instr, arg) 
def parse_instructions(input: List[str]) -> List[Instruction]:
    instructions = []
    for line in input:
        (instr, arg_as_str) = line.split()
        arg = int(arg_as_str)
        instructions.append((instr, arg))
    return instructions

# Execute a list of instructions, returns:
#   (True, acc) if a loop has been detected
#   (False, acc) if the program ended normally
def execute_code(instructions: List[Instruction]) -> Tuple[bool, int]:
    acc = 0
    i_ptr = 0
    already_run: List[bool]= [ False for i in range(len(instructions))]
    while i_ptr < len(instructions):
        (instr, arg) = instructions[i_ptr]
        if already_run[i_ptr]:
            return (True, acc)
        already_run[i_ptr] = True
        if instr == "acc":
            acc += arg
        if instr == "jmp":
            i_ptr += arg
        else:
            i_ptr += 1
    return (False, acc)

# Create a patched list of instructions, beginning at start_instr
def patch_code(instructions: List[Instruction], start_instr: int) -> Tuple[List[Instruction], int]:
    i_ptr = start_instr
    result = instructions.copy()
    while i_ptr < len(result):
        (instr, arg) = result[i_ptr]
        if instr == "nop":
            result[i_ptr] = ("jmp", arg)
            return (result, i_ptr)
        if instr == "jmp":
            result[i_ptr] = ("nop", arg)
            return (result, i_ptr)
        i_ptr += 1
    raise ValueError("Program could not be fixed!")

# Try to fix the infinite loop by iteratively trying out patched instructions 
def fix_loop(instructions: List[Tuple[str, int]]) -> int: 
    (loop_detected, acc) = (True, 0)
    patched_code = instructions
    patched_instr = 0
    while loop_detected:
        # print(patched_code, end=" -> ")
        (loop_detected, acc) = execute_code(patched_code)
        # print((loop_detected, acc))
        if loop_detected:
            (patched_code, patched_instr) = patch_code(instructions, patched_instr)
            patched_instr += 1
    return acc

def part1(input: List[str]) -> int:
    instructions = parse_instructions(input)
    (loop_detected, result) = execute_code(instructions)
    return result

def part2(input: List[str]) -> int:
    instructions = parse_instructions(input)
    result = fix_loop(instructions)
    return result

def main():    

    # Official input
    input = read_inputfile("input08.txt")

    print("The solution for part 1 on the official input is %d" % (part1(input)))
    print("The solution for part 2 on the official input is %d" % (part2(input)))

if __name__ == "__main__": 
    main()

