#!/usr/bin/env python3

import re
from typing import List

from utils import read_inputfile

Deck = List[int]

class Game:

    def __init__(self, decks: List[Deck]):
        self.player1 = decks[0]
        self.player2 = decks[1]
        self.round = 0

    def play_round(self, debug=True):
        if self.is_finished():
            return
        self.round += 1 
        card1 = self.player1[0]
        card2 = self.player2[0]
        if debug:
            print("-- Round %s --" % self.round)
            print("Player 1's deck: %s" % ", ".join([ str(i) for i in self.player1 ]))
            print("Player 2's deck: %s" % ", ".join([ str(i) for i in self.player2 ]))
            print("Player 1 plays: %d" % card1)
            print("Player 2 plays: %d" % card2)
        if card1 > card2:
            if debug:
                print ("Player 1 wins the round!")
            self.player1 = self.player1[1:] + [card1, card2]
            self.player2 = self.player2[1:]
        else:
            if debug:
                print ("Player 2 wins the round!")
            self.player1 = self.player1[1:]
            self.player2 = self.player2[1:] + [card2, card1]
  
    def is_finished(self):
        return self.player1 == [] or self.player2 == []

    def play_game(self, debug=True):
        while not self.is_finished():
            self.play_round(debug)
        if debug:
            print("== Post-game results ==")
            print("Player 1's deck: %s" % ", ".join([ str(i) for i in self.player1 ]))
            print("Player 2's deck: %s" % ", ".join([ str(i) for i in self.player2 ]))
        winners_deck = []
        if self.player1 == []:
             winners_deck = self.player2
        else:
             winners_deck = self.player1
        score = 0
        for i, card in enumerate(reversed(winners_deck), start=1):
            score += i * card
        return score
            
def read_decks(input) -> List[Deck]:
    player = 0
    decks : List[Deck] = []
    deck : Deck = []
    for line in input:
        if re.match("Player (\d):", line):
            player =+ 1
            deck = []
            if player > 0:
                decks.append(deck)
        if re.match("\d", line):
            deck.append(int(line))
    if player > 0:
        decks.append(deck)
    return decks
        

def part1(input):
    decks = read_decks(input)
    game = Game(decks)
    score = game.play_game(debug=True)
    return score

def part2(input):
    result = 0
    return result

def main():    

    # Official input
    input = read_inputfile("input22.txt")

    print("The solution for part 1 on the official input is %d" % (part1(input)))
    print("The solution for part 2 on the official input is %d" % (part2(input)))

if __name__ == "__main__": 
    main()

