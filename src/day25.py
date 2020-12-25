#!/usr/bin/env python3

import re
import os
import sys

from utils import read_inputfile

DIV = 20201227

def transform(subject: int, loop_size: int):
    value = 1
    for i in range(0, loop_size):
        value = subject * value 
        value = value % DIV 
    return value

def guess_loop_size(public_key: int):
    subject = 7
    loop_size = 1
    value = 1
    while True:
        if loop_size % 100000 == 0:
            print(loop_size)
        value = (subject * value) % DIV
        if value == public_key:
            return loop_size
        loop_size += 1

def part1(input):
    (public_key1, public_key2) = input
    print("Public key 1: %d" % public_key1)
    print("Public key 2: %d" % public_key2)
    loop_size1 = guess_loop_size(public_key1)
    loop_size2 = guess_loop_size(public_key2)
    print("Loop size 1: %d" % loop_size1)
    print("Loop size 2: %d" % loop_size2)
    encryption_key1 = transform(public_key2, loop_size1)
    encryption_key2 = transform(public_key1, loop_size2)
    print("Encryption key: %d" % encryption_key1)
    assert(encryption_key1 == encryption_key2)
    return encryption_key1

def main():    

    # Official input
    input = (1614360, 7734663)

    print("The solution for part 1 on the official input is %d" % (part1(input)))

if __name__ == "__main__": 
    main()

