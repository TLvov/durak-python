from enum import IntEnum


class Rank(IntEnum):
    SIX = 1
    SEVEN = 2
    EIGHT = 3
    NINE = 4
    TEN = 5
    JACK = 6
    QUEEN = 7
    KING = 8
    ACE = 9


class Suit(IntEnum):
    SPADE = 1
    HEART = 2
    CLUB = 3
    DIAMOND = 4


class Card:
    def __init__(self, rank: Rank, suit: Suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{str(self.rank)} {str(self.suit)}"

    def value(self, trump: Suit):
        value = int(self.rank)
        if self.suit == trump:
            value += 9
        return value


def initialize_deck():
    cards = _generate_cards()
    return _shuffle_cards(cards)


def _generate_cards():
    cards = []
    for suit in Suit:
        for rank in Rank:
            cards.append(Card(rank, suit))
    return cards


# Fisher-Yates Shuffle
def _shuffle_cards(cards: list[Card]):
    from random import randint
    for i in range(len(cards)-1, 0, -1):
        j = randint(0, i)

        cards[i], cards[j] = cards[j], cards[i]
    return cards


def deal_cards(cards: list[Card], trump: Suit):
    from players import Player, Enemy
    player_hand = []
    enemy_hand = []
    for i in range(12):
        if i % 2 == 0:
            player_hand.append(cards.pop(0))
        else:
            enemy_hand.append(cards.pop(0))
    lowest_player_trump = _lowest_held_trump(player_hand, trump)
    lowest_enemy_trump = _lowest_held_trump(enemy_hand, trump)
    if lowest_enemy_trump < lowest_player_trump:
        return Enemy(enemy_hand), Player(player_hand), cards
    else:
        return Player(player_hand), Enemy(enemy_hand), cards


def _lowest_held_trump(hand: list[Card], trump: Suit):
    lowest_trump = 19
    for card in hand:
        if card.suit == trump and card.value(trump) < lowest_trump:
            lowest_trump = card.value(trump)
    return lowest_trump
