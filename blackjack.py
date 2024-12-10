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

def deal_card(turn):
    selected_card = random.choice(deck)
    turn.append(selected_card)
    deck.remove(selected_card)
    return selected_card

result = deal_card([])

print(result)