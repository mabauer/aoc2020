#!/usr/bin/env python3


from typing import Dict
from utils import read_inputfile

def play(input, turns=2020):
    numbers: Dict[int, int] = {}

    # Play the first rounds based on the input
    last_spoken = 0
    for turn in range(1, len(input)+1):
        last_spoken = input[turn-1]
        numbers[last_spoken] = turn
        # print("%d: %d -- %s" % (turn, last_spoken, numbers))

    # Now, play the actual game
    # Note: we always consider the last (i.e. the previous) turn!
    for last_turn in range(len(input), turns):
        turn = last_turn + 1
        # Did we have the last spoken number before?
        if last_spoken in numbers:
            number = last_turn  - numbers[last_spoken]
        else:
            number = 0
        numbers[last_spoken] = last_turn
        last_spoken = number
        # print("%d: %d -- %s" % (turn, last_spoken, numbers))
    return last_spoken

def main():    

    # Official input
    # input = read_inputfile("input15.txt")
    input = [9,6,0,10,18,2,1]

    print("The solution for part 1 on the official input is %d" % (play(input)))
    print("The solution for part 2 on the official input is %d" % (play(input, 30000000)))

if __name__ == "__main__": 
    main()

