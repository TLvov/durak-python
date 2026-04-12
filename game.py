class Game:
    def __init__(self, deck):
        from card import deal_cards
        self.trump = deck[-1].suit
        print(f"Trump is: {str(self.trump)}\n")
        self.attacker, self.defender, self.deck = deal_cards(
            deck, self.trump)
        winner = self._play_game()

    # Function in charge of managing multiple rounds.
    # Returns who the winner is.

    def _play_game(self):
        someone_won, swap_needed = self._play_round([])
        if someone_won and not self._check_for_tie():
            return self._find_winner()
        if swap_needed:
            self.attacker, self.defender = self.defender, self.attacker
        return self._play_game()

    # Function in charge of managing multiple turns.
    # Returns two Booleans, first is whether someone won,
    # second is if swap is needed.

    def _play_round(self, cards_played):
        if self.attacker.can_attack(cards_played):
            attacking_card = self.attacker.attack(cards_played)
            if attacking_card is None:
                return self._discard()
            else:
                cards_played.append(attacking_card)
        else:
            return self._discard()

        if self.defender.can_defend(attacking_card, self.trump):
            defending_card = self.defender.defend(
                attacking_card, self.trump)
            if defending_card is None:
                return self._pickup(cards_played)
            else:
                cards_played.append(defending_card)
        else:
            return self._pickup(cards_played)

        return self._play_round(cards_played)

    def _discard(self):
        attacker_won, self.deck = self.attacker.draw_to_six(self.deck)
        defender_won, self.deck = self.defender.draw_to_six(self.deck)
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
