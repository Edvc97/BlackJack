from blackjack_card_class import ranks, suits, Card
from random import shuffle



class Deck:

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))

        
    def __str__(self):
        deck_comp = ''

        for card in self.deck:
            deck_comp += '\n' + str(card)
        
        return "Deck has: " + deck_comp

    def shuffle(self):
            shuffle(self.deck)
    
    def deal(self):
        return self.deck.pop()
