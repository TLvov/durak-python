def main():
    from card import initialize_deck
    from game import Game

    cards = initialize_deck()
    game = Game(cards)


if __name__ == "__main__":
    main()
