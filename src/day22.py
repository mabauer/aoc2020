#!/usr/bin/env python3

import re
from typing import List, Tuple

from utils import read_inputfile

Deck = List[int]

class Game:

    def __init__(self, decks: List[Deck], debug=True):
        self.deck_player1 = decks[0]
        self.deck_player2 = decks[1]
        self.debug = debug
        self.round = 0


    def play_round(self):
        if self.is_finished():
            return
        self.round += 1 
        card1 = self.deck_player1[0]
        card2 = self.deck_player2[0]
        if self.debug:
            print("-- Round %s --" % self.round)
            print("Player 1's deck: %s" % ", ".join([ str(i) for i in self.deck_player1 ]))
            print("Player 2's deck: %s" % ", ".join([ str(i) for i in self.deck_player2 ]))
            print("Player 1 plays: %d" % card1)
            print("Player 2 plays: %d" % card2)
        if card1 > card2:
            if self.debug:
                print ("Player 1 wins the round!")
            self.deck_player1 = self.deck_player1[1:] + [card1, card2]
            self.deck_player2 = self.deck_player2[1:]
        else:
            if self.debug:
                print ("Player 2 wins the round!")
            self.deck_player1 = self.deck_player1[1:]
            self.deck_player2 = self.deck_player2[1:] + [card2, card1]
  
    def is_finished(self):
        return self.deck_player1 == [] or self.deck_player2 == []


    def play(self):
        while not self.is_finished():
            self.play_round()
        winner = 0
        if self.deck_player1 == []:
            winner = 2
        else:
            winner = 1
        if self.debug:
            print("== Post-game results ==")
            print("Player 1's deck: %s" % ", ".join([ str(i) for i in self.deck_player1 ]))
            print("Player 2's deck: %s" % ", ".join([ str(i) for i in self.deck_player2 ]))       
            print("The winner is player %d!" % winner)
        return winner

    def compute_score(self):
        winners_deck = []
        if self.deck_player1 == []:
             winners_deck = self.deck_player2
        else:
             winners_deck = self.deck_player1
        score = 0
        for i, card in enumerate(reversed(winners_deck), start=1):
            score += i * card
        return score


class RecursiveGame(Game):

    game_no = 0

    def __init__(self, decks: List[Deck], debug=True):
        super().__init__(decks, debug)
        self.previous_decks : List[Tuple[Deck, Deck]] = []
        RecursiveGame.game_no += 1
        self.id = RecursiveGame.game_no

    def play_round(self):
        if self.is_finished():
            return
        self.round += 1 
        self.previous_decks.append((self.deck_player1.copy(), self.deck_player2.copy()))
        card1 = self.deck_player1[0]
        card2 = self.deck_player2[0]
        if self.debug:
            print("-- Round %s (Game %s) --" % (self.round, self.id))
            print("Player 1's deck: %s" % ", ".join([ str(i) for i in self.deck_player1 ]))
            print("Player 2's deck: %s" % ", ".join([ str(i) for i in self.deck_player2 ]))
            print("Player 1 plays: %d" % card1)
            print("Player 2 plays: %d" % card2)
        self.deck_player1 = self.deck_player1[1:]
        self.deck_player2 = self.deck_player2[1:]
        winner = 0
        if card1 <= len(self.deck_player1) and card2 <= len(self.deck_player2):
            if self.debug:
                print("Playing a sub-game to determine the winner...")
            # Note that only the first few cards in the decks form the decks for the sub-game!!
            subgame = RecursiveGame([self.deck_player1[:card1].copy(), self.deck_player2[:card2].copy()]) 
            winner = subgame.play()
            if self.debug:
                print("...anyway, back to game %s." % self.id)
        elif card1 > card2:
            winner = 1
        else:
            winner = 2
        if winner == 1:
            if self.debug:
                print ("Player 1 wins round %d of game %d" % (self.round, self.id))
            self.deck_player1 = self.deck_player1 + [card1, card2]
        else:
            if self.debug:
                print ("Player 2 wins round %d of game %d" % (self.round, self.id))
            self.deck_player2 = self.deck_player2 + [card2, card1]
  
    def is_finished(self):
        if self.deck_player1 == [] or self.deck_player2 == []:
            return True
        if (self.deck_player1, self.deck_player2) in self.previous_decks:
            # We already had these decks => Player 2 looses
            if self.debug:
                print("Player 1's deck: %s" % ", ".join([ str(i) for i in self.deck_player1 ]))
                print("Player 2's deck: %s" % ", ".join([ str(i) for i in self.deck_player2 ]))
                print("Recursion detected before round %d in game %d => winner is 1 (always)" % (self.round, self.id))
            self.deck_player2 = []
            return True
        return False

    def play(self):
        while not self.is_finished():
            self.play_round()
        winner = 0
        if self.deck_player1 == []:
            winner = 2
        else:
            winner = 1
        if self.debug:
            if self.id == 1:
                print("== Post-game results ==")
                print("Player 1's deck: %s" % ", ".join([ str(i) for i in self.deck_player1 ]))
                print("Player 2's deck: %s" % ", ".join([ str(i) for i in self.deck_player2 ]))
        
            print("The winner of game %d is: %d" % (self.id, winner))
        return winner

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
    game = Game(decks, debug=True)
    game.play()
    score = game.compute_score()
    return score

def part2(input):
    decks = read_decks(input)
    game = RecursiveGame(decks, debug=True)
    game.play()
    score = game.compute_score()
    return score

def main():    

    # Official input
    input = read_inputfile("input22.txt")

    print("The solution for part 1 on the official input is %d" % (part1(input)))
    print("The solution for part 2 on the official input is %d" % (part2(input)))

if __name__ == "__main__": 
    main()

