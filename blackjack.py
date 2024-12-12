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
        if card in range(1,11):
            total += card
        elif card in face:
            total += 1
        else:
            if total > 11:
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
        stay_or_hit = input("1: Stay\n2: Hit")
    if total(dealer_hand) > 16:
        dealer_in = False
    else:
        deal_card(dealer_hand)