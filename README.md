# Durak Python
### Programmed by Tihon Lvov
A text version of the traditional Russian card game **Durak**.

## Project Purpose
I wrote this program as a capstone project for the Sigma Labs pre-course to showcase my python skills.

## How to run
Download durak.py and resources folder, run durak.py

## What is Durak?
[Wikipedia page](https://en.wikipedia.org/wiki/Durak)

My adaptation is a simple one-versus-one version of the game, where you play against a very basic bot that will always play its lowest valued card.

### Set-up
The game uses a reduced deck consisting of cards ranked six through ace. One suit is determined as the trump after shuffling the deck, the suit of the bottom card in the deck is considered the trump suit for the entire game session. Each player draws to six cards and proceed to take turns attacking and defending against each other. The player with the lowest trump card will attack first. 

### Basic play
At the beginning of an attack, the attacker can 'attack' with any card in hand. The defender has to choose a card to 'defend' with, this can be any card in their hand that is of the same suit as the attacking card and is of a higher rank than the attacking card. Cards of the trump suit can be used to defend against any other suit and evade the need to be of a higher rank, as such: trump-suited cards can be considered of a higher 'value'. If the defender successfully defends, the attacker will have an opportunity to continue the attack. Subsequent attacks have to be of a rank already used in that round, either in attack or defense. For example, attacker attacks with a six of clubs, defender defends with a seven of clubs, the attacker is now allowed to attack again with any sixes or sevens in their hand.

At the end of each round, each player will draw to six cards as long as there are cards remaining in the deck. Within a round, a 'pile' will form consisting of every card used to attack or defend in that round. Cards are permanently removed from the game when the attacking player discards the pile. As long as a pile exists, the attacker can choose to discard. Alternatively, if the pile exists and the attacker has no eligible cards to attack with, they will be forced to discard the pile. If a discard occurs, the players will swap roles. A defending player can always choose to pick up the pile. Alternatively, if the defender has no eligible cards to defend against the most recent attack, they will be forced to pick up the pile. A player's hand can exceed six cards by picking up the pile. If the defender picks up, the attack will be able to begin a new attack. The goal of the game is to run out of cards after the draw step at end-of-round, i.e., the deck is empty when the player needs to draw to six cards. It is possible for both players to run out of cards while the deck is empty, i.e., the defender successfully defends against the attackers last attack with their final card. This results in a tie. 
