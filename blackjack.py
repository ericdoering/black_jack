import random

deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 
        2, 3, 4, 5, 6, 7, 8, 9, 10, 
        2, 3, 4, 5, 6, 7, 8, 9, 10, 
        2, 3, 4, 5, 6, 7, 8, 9, 10,
        'J', 'Q', 'K', 'A',
        'J', 'Q', 'K', 'A',
        'J', 'Q', 'K', 'A',
        'J', 'Q', 'K', 'A']

player_hand = []
dealer_hand = []

player_in = True
dealer_in = True

def deal_card(turn):
    selected_card = random.choice(deck)
    turn.append(selected_card)
    deck.remove(selected_card)
    return selected_card


def total(turn):
    total = 0
    face = ['J', 'Q', 'K']

    for card in turn:
        if card in range(1, 11):
            total += card
        elif card in face:
            total += 10
        else:  
            if total > 10:
                total += 1
            else:
                total += 11
    return total
    
def reveal_dealer_hand():
    if len(dealer_hand) == 2:
        return dealer_hand[0]
    elif len(dealer_hand) > 2:
        return dealer_hand[0], dealer_hand[1]
    

for _ in range(2):
    deal_card(dealer_hand)
    deal_card(player_hand)


print ("DEALER HAND", dealer_hand)
print ("PLAYER HAND", player_hand)

while player_in or dealer_in:
    print(f"Dealer has {reveal_dealer_hand()} and X")
    print(f"You have {player_hand} for a total of {total(player_hand)}")
    if player_in:
        while True:
            stay_or_hit = input("1: Stay\n2: Hit\n")
            if stay_or_hit in ['1', '2']:
                break
            print("Invalid choice. Please choose 1 or 2.")
    if total(dealer_hand) > 16:
        dealer_in = False
    else:
        deal_card(dealer_hand)
    if stay_or_hit == '1':
        player_in = False
    else: 
        deal_card(player_hand)
    if total(player_hand) >= 21:
        break
    elif total(dealer_hand) >= 21:
        break

if total(player_hand) == 21:
    print(f"Player has blackjack!\n {player_hand}")

elif total(dealer_hand) == 21:
    print(f"Dealer has blackjack!\n {dealer_hand}")

elif total(player_hand) > 21:
    print(f"Player has busted!\n {player_hand}")

elif total(dealer_hand) > 21:
    print(f"Dealer has busted! \n {dealer_hand}" )

elif 21 - total(dealer_hand) > 21 - total(player_hand):
    print(f"Dealer has {total(dealer_hand)} and player has {total(player_hand)}.\n Player Wins!")
elif 21 - total(player_hand) > 21 - total(dealer_hand):
    print(f"Player has {total(player_hand)} and dealer has {total(dealer_hand)}.\n Dealer Wins!")