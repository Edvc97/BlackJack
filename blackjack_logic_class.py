from blackjack_chips_class import Chips
from blackjack_card_class import playing
from blackjack_deck_class import Deck
from blackjack_hand_class import Hand

def take_bet(chips):    
    while True:
        try:
            chips.bet = abs(int(input("How much will you bet? : ")))
            if chips.bet > chips.total:
                print("Not enough funds!")
                raise ValueError()
        except:
            print("Try again!")
            continue
        else:
            print("Bet accepted!")
            break
        
def hit(deck,hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop
    while True:
        x = input("\nHit or Stand? Enter 'H' or 'S': ")
        if x[0].lower() == 'h':
            hit(deck,hand)
            print('\nCurrent cards: ',*hand.cards, sep = '\n')
            print("\n")
        elif x[0].lower() == 's':
            print("Player stands, Dealer's turn.")
            playing = False
        else:
            print("Sorry, please enter 'H' or 'S' Only.")
            continue
        break
 
def show_some(player,dealer):
    #showing only one of dealer's cards
    print("\nDealer's hand: ")
    print("\tSecond card hidden")
    print(dealer.cards[0])   
    
    #show all of player's cards
    print("\nPlayer's hand: ")
    for card in player.cards:
        print(card)

def show_all(player,dealer):
    #show all cards in both the dealer's and player's hand, show total value of each
    #Dealer
    print("\nDealer's hand: ")
    for card in dealer.cards:
        print(card)
    print(f"\n Value of Dealer's hand: {dealer.value}")
   
    #Player
    print("\nPlayer's hand: ")  
    for card in player.cards:
        print(card)
    print(f"\n Value of Player's hand: {player.value}")


def player_busts(chips):
    print("Player busted!")
    chips.lose_bet()

def player_wins(chips):
    print("Player wins!")
    chips.win_bet()

def dealer_busts(chips):
    print("Player wins! Dealer busted!")
    chips.win_bet()
    
def dealer_wins(chips):
    print("Dealer wins!!")
    chips.lose_bet()
    
def push():
    print("Dealer and Player tied! PUSH")

# Set up the Player's chips
playersChips = Chips()

while True:
    # Print an opening statement
    print("\n")
    print("LET THE GAME OF BLACKJACK BEGIN!!\n\nGet as close to 21 as you can without going over!\nDealer hits until she reaches 17. Aces count as 1 or 11.\n")
    print("CURRENT CHIPS: {0}".format(playersChips.total))

    
    # Create & shuffle the deck, deal two cards to each player
    gameDeck = Deck()
    gameDeck.shuffle() # I like to shuffle twice :)
    gameDeck.shuffle()
    
    sucker = Hand() #Player
    heartless = Hand() #Dealer

    sucker.add_card(gameDeck.deal())#Two to the Player
    sucker.add_card(gameDeck.deal())
    sucker.adjust_for_ace() #Accounting for two aces (value = 11) in a row
    
    heartless.add_card(gameDeck.deal())#Two to the Dealer
    heartless.add_card(gameDeck.deal())
    sucker.adjust_for_ace() #Accounting for two aces (value = 11) in a row

    
    
    # Prompt the Player for their bet
    take_bet(playersChips)

    
    # Show cards (but keep one dealer card hidden)
    show_some(sucker, heartless)

    
    while playing:  # recall this variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
        hit_or_stand(gameDeck, sucker)
        
        # Show cards (but keep one dealer card hidden)
        show_some(sucker, heartless)

 
        
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if sucker.value > 21:
            player_busts(playersChips)
            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if sucker.value <= 21:
        while heartless.value < 17:
            hit(gameDeck, heartless)
    
        # Show all cards
        show_all(sucker, heartless)
    
        # Run different winning scenarios
        if heartless.value > 21:
             dealer_busts(playersChips)
        elif sucker.value > heartless.value:
            player_wins(playersChips)
        elif sucker.value < heartless.value:
            dealer_wins(playersChips)
        else:
            push()


    
    # Inform Player of their chips total 
    print("\n")
    print(f"Player currently has {playersChips.total} chips total!")
    
    # Ask to play again
    again = input("Do you want to play again? 'Y' or 'N': ")
    if again[0].lower() == 'y':
        if playersChips.total > 0:
            playing = True
            continue
        else:
            print("Not enough funds! The game cannot continue. Goodbye!")
            break

    else:
        print("Thank you for playing!")
        break
