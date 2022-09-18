# This a game logic module that contains majority of the processes that will be used in the blackjack.py
# Such approach should keep the main body neat and clean
# --------------------
#    BLACKJACK GAME   
# --------------------
#
# ANY TIPS AND TRICS ARE MORE THAN WELCOME, EITHER IN THE CODE (PLEASE COMMENT APPROPRIETALY) OR SEPARATELY
# ---------------------------------------------------------------------------------------------------------

import random

suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
ranks = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace"]
values = {"Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10, "Jack": 10, "Queen": 10, "King": 10, "Ace": 11}
playing = True

class Card:
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return(f"{self.rank} of {self.suit}")

class Deck:

    def __init__(self):
        self.deck = []

        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))
    
    def __str__(self):
        deck = ""
        for card in self.deck:
            deck += "\n " + card.__str__()
        return "The deck contains: " + deck

    def shuffle(self):
        random.shuffle(self.deck)
    
    def deal(self):
        card = self.deck.pop()
        return card

class Hand:

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
    
    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]

        if card.rank == "Ace":
            self.aces += 1

    def adjust_aces(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

class Chips:
    
    def __init__(self, total=200):
        self.total = total
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet

def take_bet(chips):
    
    while True:
        try:
            chips.bet = int(input("Please, place your bet.\n"))
        except ValueError:
            print("The bet value must be an integer.")
        else:
            if chips.bet > chips.total:
                print("The bet cannot exceed ", chips.total)
            else:
                break

def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_aces()

def hit_or_stand(deck, hand):
    global playing

    while True:
        x = input("Do you want to hit (h), or stand (s)? ")

        if x.lower() == "h":
            hit(deck, hand)
        elif x.lower() == "s":
            print("Player stands.")
            playing = False
        else:
            print("Unrecognized, please try again.")
            continue
        break

def show_some(player, dealer):
    print("\nDealer's hand:")
    print(" Hidden Card ")
    print(" ", dealer.cards[1])
    print("\nPlayer's hand:", *player.cards, sep="\n")

def show_all(player, dealer):
    print("\nDealer's hand: ", *dealer.cards, sep="\n")
    print("Dealer's hand value is ", dealer.value)
    print("\nPlayer's hand: ", *player.cards, sep="\n")
    print("Player's hand value is ", player.value)

def player_busts(player, dealer, chips):
    print("Player busted!")
    chips.lose_bet

def player_wins(player, dealer, chips):
    print("Player wins!")
    chips.win_bet

def dealer_busts(player, dealer, chips):
    print("Dealer busted!")
    chips.win_bet

def dealer_wins(player, dealer, chips):
    print("Dealer wins!")
    chips.lose_bet

def tie(player, dealer):
    print("It's a tie!")
