from enum import Enum


class Rank(Enum):
    SIX = 1
    SEVEN = 2
    EIGHT = 3
    NINE = 4
    TEN = 5
    JACK = 6
    QUEEN = 7
    KING = 8
    ACE = 9


class Suit(Enum):
    SPADE = 1
    HEART = 2
    CLUB = 3
    DIAMOND = 4


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{str(self.rank)} {str(self.suit)}"

    def value(self, trump):
        value = int(self.rank)
        if self.suit == trump:
            value += 9
        return value
