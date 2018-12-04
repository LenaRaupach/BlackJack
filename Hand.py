import Deck

class Hand:

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def __str__(self):
        return str(self.cards)

    def add_value(self, card):
        if card.split()[0] == "Ace":
            if self.value + 11 > 21:
                self.value += 1
            else:
                self.value += Deck.values[card.split()[0]]
        else:
            self.value += Deck.values[card.split()[0]]

    def add_card(self, card):
        self.cards.append(card)
        self.add_value(card)
