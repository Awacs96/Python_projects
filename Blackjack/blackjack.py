from game_logic import *

while True:

    print("Welcome to the game! The goal is to get as close to 21 as you can.")
    print("Player starts with 200 chips.")

    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    dealer_hand = Hand()

    player_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    player_chips = Chips()
    take_bet(player_chips)

    show_some(player_hand, dealer_hand)

    while playing:
        hit_or_stand(deck, player_hand)
        show_some(player_hand, dealer_hand)

        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            break

    if player_hand.value <= 21:

        while dealer_hand.value < 17:
            hit(deck, dealer_hand)
        
        show_all(player_hand, dealer_hand)

        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)
        else:
            tie(player_hand, dealer_hand)
        
    print("\nPlayer's chips stand at ", player_chips.total)

    new_game = input("Would you like to play another hand? Y/N\n")

    if new_game[0].lower() == "y":
        playing = True
        continue
    else:
        print("Thank you for playing.")
        break