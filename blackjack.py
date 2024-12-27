# Importing the python module "random".
# Python's random module uses the "Mersenne Twister" algroithm to conduct the randomization.
import random

# Setting the 52 card deck. Suites are irrelevant for blackjack and therefore don't necessarily need to be included.
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 
        2, 3, 4, 5, 6, 7, 8, 9, 10, 
        2, 3, 4, 5, 6, 7, 8, 9, 10, 
        2, 3, 4, 5, 6, 7, 8, 9, 10,
        'J', 'Q', 'K', 'A',
        'J', 'Q', 'K', 'A',
        'J', 'Q', 'K', 'A',
        'J', 'Q', 'K', 'A']

# Setting the player hand and dealer hand which will store their cards.
player_hand = []
dealer_hand = []

# These boolean values will initiate whether each player is still in for the game.
player_in = True
dealer_in = True

# This function draws a random card from the deck appends it to either the player of dealer's hand and removes it from the deck
def deal_card(turn):
    selected_card = random.choice(deck)
    turn.append(selected_card)
    deck.remove(selected_card)
    return selected_card


# This function calculates the total based on the type of cards that are drawn.
def total(turn):
    total = 0
    face = ['J', 'Q', 'K']
    aces = 0

    for card in turn:
        if isinstance(card, int):
            total += card
        elif card in face:
            total += 10
        elif card == 'A':
            aces += 1
    
    # Handle Aces last
    for _ in range(aces):
        if total + 11 > 21:
            total += 1
        else:
            total += 11

    return total
    
# This function will display the dealers hand as the game goes on.
def reveal_dealer_hand():
    if len(dealer_hand) == 1:
        return dealer_hand[0]
    elif len(dealer_hand) >= 2:
        return dealer_hand[0], dealer_hand[1]
    

# Run a loop that will alternate between the player and the dealer.
for _ in range(2):
    deal_card(dealer_hand)
    deal_card(player_hand)


print ("DEALER HAND", dealer_hand)
print ("PLAYER HAND", player_hand)

# A loop that will run the actual game
while player_in or dealer_in:
    # If both players are out of the game, stop the loop
    if not player_in and not dealer_in:
        break
    print(f"Dealer has {reveal_dealer_hand()}")
    print(f"You have {player_hand} for a total of {total(player_hand)}")
    if player_in:
        while True:
            stay_or_hit = input("1: Stay\n2: Hit\n").strip()
            if stay_or_hit in ['1', '2']:
                break
            print("Invalid choice. Please enter 1 or 2.")
            # The dealer will not hit if they currently have a total of 16 or more.
    if total(dealer_hand) > 16:
        dealer_in = False
    else:
        deal_card(dealer_hand)
    if stay_or_hit == '1':
        player_in = False
    else: 
        deal_card(player_hand)
    # These two conditions occur when the player or the dealer bust.
    if total(player_hand) >= 21:
        break
    elif total(dealer_hand) >= 21:
        break

# Winning and losing scenerios for player and dealer.
if total(player_hand) == 21:
    print(f"Player has blackjack!\n {player_hand}")

elif total(dealer_hand) == 21:
    print(f"Dealer has blackjack!\n {dealer_hand}")

elif total(player_hand) > 21:
    print(f"Player has busted!\n {player_hand}")

elif total(dealer_hand) > 21:
    print(f"Dealer has busted!\n {dealer_hand}" )

elif total(player_hand) == total(dealer_hand):
    print(f"Player and dealer both have {total(player_hand)}. It's a tie!")

elif 21 - total(dealer_hand) > 21 - total(player_hand):
    print(f"Dealer has {total(dealer_hand)} and player has {total(player_hand)}.\n Player Wins!")
elif 21 - total(player_hand) > 21 - total(dealer_hand):
    print(f"Player has {total(player_hand)} and dealer has {total(dealer_hand)}.\n Dealer Wins!")