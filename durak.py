from card import Card, Rank, Suit


def main():
    cards = shuffle_cards(generate_cards())
    for card in cards:
        print(card)
    trump = cards[len(cards)-1].suit
    print(f"\nThe trump is {trump}")


def generate_cards():
    cards = []
    for suit in Suit:
        for rank in Rank:
            cards.append(Card(rank, suit))
    return cards


# Fisher-Yates Shuffle
def shuffle_cards(cards):
    from random import randint
    for i in range(len(cards)-1, 0, -1):
        j = randint(0, i+1)

        cards[i], cards[j] = cards[j], cards[i]
    return cards


if __name__ == "__main__":
    main()
