class Game:
    def __init__(self, deck):
        from Resources.card import deal_cards
        self.trump = deck[-1].suit
        self.deck = deck
        for card in self.deck:
            if card.suit == self.trump:
                card.value += 9
        print(f"Trump is: {str(self.trump)}\n")
        self.attacker, self.defender = deal_cards(
            self.deck, self.trump)

    # Function in charge of managing multiple rounds.
    # Returns who the winner is.

    def play_game(self):
        someone_won, swap_needed = self._play_round([])

        if someone_won:
            if self._check_for_tie():
                return None
            return self._find_winner()

        if swap_needed:
            self.attacker, self.defender = self.defender, self.attacker

        return self.play_game()

    # Function in charge of managing multiple turns.
    # Returns two Booleans, first is whether someone won,
    # second is if swap is needed.

    def _play_round(self, cards_played):
        if not self.attacker.can_attack(cards_played):
            return self._discard()

        attacking_card = self.attacker.attack(cards_played)
        if attacking_card is None:
            return self._discard()
        cards_played.append(attacking_card)

        if not self.defender.can_defend(attacking_card, self.trump):
            return self._pickup(cards_played)

        defending_card = self.defender.defend(attacking_card, self.trump)
        if defending_card is None:
            return self._pickup(cards_played)
        cards_played.append(defending_card)

        return self._play_round(cards_played)

    def _discard(self):
        attacker_won = self.attacker.draw_to_six(self.deck)
        defender_won = self.defender.draw_to_six(self.deck)
        return attacker_won or defender_won, True

    def _pickup(self, cards_played):
        self.defender.pickup_pile(cards_played)
        attacker_won, self.deck = self.attacker.draw_to_six(self.deck)
        return attacker_won, False

    def _check_for_tie(self):
        if len(self.attacker.hand) == len(self.defender.hand):
            return True
        return False

    def _find_winner(self):
        if len(self.attacker.hand) < len(self.defender.hand):
            return self.attacker
        return self.defender
