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

    def tokenize(self, s: str) -> List[str]:
        tokens = []
        pos = 0
        while pos < len(s):
            ch = s[pos]
            if ch.isdigit():
                token = ""
                while pos < len(s) and ch.isdigit():
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
        result = self.eval_term()        
        while self.token in ["+", "*"]:
            if self.token == "+":
                self.next_token()
                result = result + self.eval_term()
            else: 
                self.next_token()
                result = result * self.eval_term()
        if self.token is not None and self.token != ")": 
            raise ValueError("Syntax error: missing +, * or )?")
        return result
         

    def eval_number(self) -> int:
        assert self.token is not None
        return int(self.token)        

    def eval_term(self) -> int:
        if self.token is not None:
            if self.token == "(":
                self.next_token()
                result = self.eval_expr()
                if self.token != ")":
                    raise ValueError("SyntaxError: ) expected")
                self.next_token()
                return result
            if re.match("\d+", self.token) is not None:
                result = self.eval_number()
                self.next_token()
                return result
        raise ValueError("Syntax error: ( or number expected")

    def eval(self) -> int:
        self.next_token()
        return self.eval_expr()


class Expression2:

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
        result = self.eval_factor()        
        while self.token in ["*"]:
            if self.token == "*":
                self.next_token()
                result = result * self.eval_factor()
        return result
        # raise ValueError("+ or * expected")
         
    def eval_factor(self) -> int:
        result = self.eval_term()        
        while self.token in ["+"]:
            if self.token == "+":
                self.next_token()
                result = result + self.eval_term()
        return result


    def eval_number(self) -> int:
        if self.token is None:
            raise ValueError("Invalid Number")
        return int(self.token)        

    def eval_term(self) -> int:
        if self.token is not None:
            if self.token == "(":
                self.next_token()
                result = self.eval_expr()
                if self.token != ")":
                    raise ValueError(") expected")
                self.next_token()
                return result
            if re.match("\d+", self.token) is not None:
                result = self.eval_number()
                self.next_token()
                return result
        raise ValueError("( or number expected")

    def eval(self) -> int:
        self.next_token()
        return self.eval_expr()


def part1(input):
    sum = 0
    for line in input:
        result = Expression(line).eval()
        sum += result
    return sum

def part2(input):
    sum = 0
    for line in input:
        result = Expression2(line).eval()
        sum += result
    return sum

def main():    

    # Official input
    input = read_inputfile("input18.txt")

    print("The solution for part 1 on the official input is %d" % (part1(input)))
    print("The solution for part 2 on the official input is %d" % (part2(input)))

if __name__ == "__main__": 
    main()

