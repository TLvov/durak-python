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
        addressing, addressing_noun = "Enemy", "is"
        if type(self) == Player:
            addressing, addressing_noun = "You", "are"
        print(f"\n{addressing} cannot continue the attack...\n{addressing} {addressing_noun} discarding the pile and passing the attack.\n")
        return False

    def can_defend(self, attacking_card, trump):
        for card in self.hand:
            if (card.suit == attacking_card.suit or card.suit == trump) and card.value > attacking_card.value:
                return True
        addressing, opponent = "Enemy", "You"
        if type(self) is Player:
            addressing, opponent = "You", "Enemy"
        print(
            f"\n{addressing} cannot defend...\n{addressing} will pick up the pile.\n{opponent} will attack again.\n")
        return False

    def attack(self, cards_played):
        self.hand.sort(key=lambda x: x.value)

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
            print("You are discarding the pile and passing the attack.\n")
            return None

        attacking_card = self.hand.pop(card_index - 1)
        print(f"You are attacking with {attacking_card}")
        return attacking_card

    def first_attack(self):
        print(f"First strike! Attack with any card!\nYour hand:\n{self}")
        card_index = _get_valid_input(
            "Enter the number of your desired attacking card: ", 1, len(self.hand))
        attacking_card = self.hand.pop(card_index - 1)
        print(f"You are attacking with {attacking_card}")
        return attacking_card

    def defend(self, attacking_card, trump):
        self.hand.sort(key=lambda x: x.value)

        if attacking_card.suit == trump:
            print(
                f"You can defend by playing a {str(trump)} of a higher rank")
        else:
            print(
                f"You can defend by playing a {str(attacking_card.suit)} of a higher rank or any {str(trump)}")

        print(f"\nIf you would like to pickup, enter 0\nYour hand:\n{self}")

        while True:
            card_index = _get_valid_input(
                "Enter the number of your desired defending card: ", 0, len(self.hand))

            if card_index == 0:
                print(
                    "You are declining to defend and picking up the pile.\nThe enemy will attack again.\n")
                return None

            defending_card = self.hand[card_index - 1]
            if (defending_card.suit == attacking_card.suit or defending_card.suit == trump) and defending_card.value > attacking_card.value:
                self.hand.remove(defending_card)
                print(f"You are defending with {defending_card}")
                return defending_card

            print("Sorry... that card is unable to defend against the attacking card.")

    def draw_to_six(self, deck):
        if len(self.hand) == 0 and len(deck) == 0:
            return True

        cards_picked_up = 0
        while len(self.hand) < 6 and len(deck) > 0:
            self.hand.append(deck.pop(0))
            cards_picked_up += 1
        addressing = "Enemy has"
        if type(self) == Player:
            addressing = "You have"
        print(f"{addressing} picked up {cards_picked_up} card(s), there are {len(deck)} card(s) remaining in the deck\n")
        return False

    def pickup_pile(self, pile):
        self.hand += pile


class Enemy(Player):
    def __init__(self, hand):
        Player.__init__(self, hand)

    def attack(self, cards_played):
        if len(cards_played) == 0:
            return self.first_attack()

        ranks_played = _get_ranks_played(cards_played)
        lowest_value = 19
        lowest_card = None
        for card in self.hand:
            if card.rank in ranks_played and card.value < lowest_value:
                lowest_value = card.value
                lowest_card = card
        print(f"Enemy is attacking with {lowest_card}")
        self.hand.remove(lowest_card)
        return lowest_card

    def first_attack(self):
        lowest_value = 19
        lowest_card = None
        for card in self.hand:
            if card.value < lowest_value:
                lowest_value = card.value
                lowest_card = card
        print(f"Enemy is attacking with {lowest_card}")
        self.hand.remove(lowest_card)
        return lowest_card

    def defend(self, attacking_card, trump):
        lowest_value = 19
        lowest_card = None
        for card in self.hand:
            if (card.suit == attacking_card.suit or card.suit == trump) and card.value > attacking_card.value and card.value < lowest_value:
                lowest_value = card.value
                lowest_card = card
        print(f"Enemy is defending with {lowest_card}")
        self.hand.remove(lowest_card)
        return lowest_card


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
    ranks_played = {enumerate}

    for card in cards_played:
        ranks_played.add(card.rank)

    return ranks_played
