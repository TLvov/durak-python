def main():
    from Resources.card import initialize_deck
    from Resources.game import Game
    from Resources.players import Player, Enemy

    playing = True
    while playing:
        cards = initialize_deck()
        game = Game(cards)
        winner = game.play_game()
        if type(winner) is Player:
            print("\nYou have won!")
        elif type(winner) is Enemy:
            print("\nYou have lost...")
        else:
            print("\nIt was a tie!")
        playing = play_again()


def play_again():
    while True:
        yes_no = input("\nWould you like to play again? Y/N: ")
        if yes_no == "Y":
            return True
        if yes_no == "N":
            return False
        print("Sorry... Please only enter 'Y' or 'N'\n")


if __name__ == "__main__":
    main()
