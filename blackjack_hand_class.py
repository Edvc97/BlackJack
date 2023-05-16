from blackjack_card_class import values

class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,card):
        self.cards.append(card)
        nameOfCard = str(card).split()
        self.value += values[nameOfCard[0]]
    
    def adjust_for_ace(self):
        if self.value > 21: # checking if total value of cards is over 21
            for card in self.cards: 
                if str(card).split()[0] == 'Ace': #checking if any card in hand is an ace
                    self.value -= 10 #subtracting 10, essentially making the the value of the ace a one, instead of 11

