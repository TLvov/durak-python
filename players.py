class Player:
    def __init__(self, hand):
        self.hand = hand

    def __str__(self):
        cards = ""
        i = 1
        for card in self.hand:
            cards += f"{i}: {card}\n"
            i += 1
        return cards

    def can_attack(self, cards_played):
        if len(cards_played) == 0:
            return True

        ranks_played = _get_ranks_played(cards_played)

        for card in self.hand:
            if card.rank in ranks_played:
                return True

        print("Attacker cannot play...")
        return False

    def can_defend(self, attacking_card, trump):
        for card in self.hand:
            if (card.suit == attacking_card.suit or card.suit == trump) and card.value(trump) > attacking_card.value(trump):
                return True
        print("Defender cannot play...")
        return False

    def attack(self, cards_played):
        if len(cards_played) == 0:
            return self.first_attack()

        ranks_played = _get_ranks_played(cards_played)
        print(f"You can attack again!\nAttack with any card of the following ranks:")
        for rank in ranks_played:
            print(str(rank))
        print(f"\nIf you would like to discard, enter 0\nYour hand:\n{self}")
        card_index = _get_valid_input(
            "Enter the number of your desired attacking card: ", 0, len(self.hand))
        if card_index == 0:
            return None
        else:
            return self.hand.pop(card_index - 1)

    def first_attack(self):
        print(f"First strike! Attack with any card!\nYour hand:\n{self}")
        card_index = _get_valid_input(
            "Enter the number of your desired attacking card: ", 1, len(self.hand))
        return self.hand.pop(card_index - 1)

    def defend(self, attacking_card, trump):
        print(
            f"You've been attacked by {attacking_card}.\nYou can defend with a higher value card of the same suit, or any trump ({str(trump)}).")
        print(f"\nIf you would like to pickup, enter 0\nYour hand:\n{self}")
        while True:
            card_index = _get_valid_input(
                "Enter the number of your desired defending card: ", 0, len(self.hand))
            if card_index == 0:
                return None
            else:
                defending_card = self.hand[card_index - 1]
                if (defending_card.suit == attacking_card.suit or defending_card.suit == trump) and defending_card.value(trump) > attacking_card.value(trump):
                    return defending_card
                print(
                    "Sorry... that card is unable to defend against the attacking card.")

    def draw_to_six(self, deck):
        if len(self.hand) == 0 and len(deck) == 0:
            return True, deck
        while len(self.hand) < 6 and len(deck) > 0:
            self.hand.append(deck.pop(0))
        return False, deck

    def pickup_pile(self, pile):
        self.hand += pile


class Enemy(Player):
    def __init__(self, hand):
        Player.__init__(self, hand)


def _get_valid_input(prompt: str, lowest_choice: int, highest_choice: int):
    while True:
        try:
            choice = int(input(prompt))
            if choice >= lowest_choice and choice <= highest_choice:
                return choice
            print("Sorry... please enter a number that corresponds with a given option\n")
        except:
            print("Sorry... please enter an integer input\n")


def _get_ranks_played(cards_played):
    ranks_played = []

    for card in cards_played:
        if not (card.rank in ranks_played):
            ranks_played.append(card.rank)

    return ranks_played
