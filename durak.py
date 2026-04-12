def main():
    from card import initialize_deck
    from game import Game
    from players import Player

    playing = True
    while playing:
        cards = initialize_deck()
        game = Game(cards)
        if game.winner is Player:
            print("You have won!")
        else:
            print("You have lost...")
        playing = play_again()


def play_again():
    while True:
        yes_no = input("Would you like to play again? Y/N: ")
        if yes_no == "Y":
            return True
        if yes_no == "N":
            return False
        print("Sorry... Please only enter 'Y' or 'N'\n")


if __name__ == "__main__":
    main()
