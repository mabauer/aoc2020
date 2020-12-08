#!/usr/bin/env python3

import re
import os
import sys

def execute_code(instructions):
    acc = 0
    i_ptr = 0
    already_run = [ False for i in range(len(instructions))]
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

def parse_instructions(input):
    instructions = []
    for line in input:
        (instr, arg_as_str) = line.split()
        arg = int(arg_as_str)
        instructions.append((instr, arg))
    return instructions

def patch_code(instructions, patched_instr):
    i_ptr = patched_instr
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


def fix_loop(instructions):
    loop_detected = True
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

def compute08(input):
    instructions = parse_instructions(input)
    (loop_detected, result) = execute_code(instructions)
    return result

def compute08b(input):
    instructions = parse_instructions(input)
    result = fix_loop(instructions)
    return result

def main():    

    # Official input
    input_file = os.path.abspath(os.path.dirname(__file__)) + os.path.sep + "input08.txt"
    with open(input_file) as f:
        input = [l.strip() for l in f]

    print("The solution for part 1 on the official input is %d" % (compute08(input)))
    print("The solution for part 2 on the official input is %d" % (compute08b(input)))

if __name__ == "__main__": 
    main()

