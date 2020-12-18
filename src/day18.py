#!/usr/bin/env python3

from abc import get_cache_token
import re
from typing import List

from utils import read_inputfile

class Expression:

    def __init__(self, s: str):
        self.debug_s = s
        self.tokens = self.tokenize(s)
        self.current = 0
        self.token = None

    def is_digit(self, ch: str) -> bool:
        if ch in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
            return True
        else:
            return False

    def tokenize(self, s: str) -> List[str]:
        tokens = []
        pos = 0
        while pos < len(s):
            ch = s[pos]
            if self.is_digit(ch):
                token = ""
                while pos < len(s) and self.is_digit(ch):
                    token = token + ch
                    pos += 1
                    if pos < len(s):
                        ch = s[pos]
                tokens.append(token)
                token = ""
            elif ch in ["(", ")", "*", "+"]:
                tokens.append(ch)
                pos += 1
            else:
                pos += 1
        return tokens


    def raise_error(self, msg: str):
        raise ValueError(str)

    def next_token(self):
        if self.current < len(self.tokens):
            self.token = self.tokens[self.current]
        else:
            self.token = None
        self.current += 1

    def eval_expr(self) -> int:
        left = self.eval_term()        
        self.next_token()
        if self.token == "+":
            self.next_token()
            return left + self.eval_expr()
        if self.token == "*":
            self.next_token()
            return left * self.eval_expr()
        return left
        # raise ValueError("+ or * expected")
         

    def eval_number(self) -> int:
        if self.token is None:
            raise ValueError("Invalid Number")
        return int(self.token)        

    def eval_term(self) -> int:
        if self.token is not None:
            if self.token == "(":
                self.next_token()
                result = self.eval_expr()
                # self.next_token()
                if self.token != ")":
                    raise ValueError(") expected")
                return result
            if re.match("\d+", self.token) is not None:
                return self.eval_number()
        raise ValueError("( or number expected")

    def eval(self) -> int:
        self.next_token()
        return self.eval_expr()


def part1(input):
    result = 0
    return result

def part2(input):
    result = 0
    return result

def main():    

    # Official input
    input = read_inputfile("input18.txt")

    print("The solution for part 1 on the official input is %d" % (part1(input)))
    print("The solution for part 2 on the official input is %d" % (part2(input)))

if __name__ == "__main__": 
    main()

