import random
faces = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
card_deck = faces * 4
random.shuffle(card_deck)
face_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': [1, 11]}
def deal_card(deck):
    if not deck:
        raise ValueError("The deck is empty!")
    return deck.pop()
def calculatedscore(hand):
    total_score = 0
    aces = 0
    for face in hand:
        if face == 'A':
            aces += 1
            total_score += face_values[face]
        else:
            total_score += face_values[face]
    while total_score > 21 and aces:
        total_score -= 10
        aces -= 1
    return total_score
def player_turn(playercard, deck, interactive=True, simulated_actions=None):
    action_index = 0
    while calculatedscore(playercard) <= 21:
        if interactive:
            action = input("Do you want to hit? (y/n) ").lower()
        else:
            if action_index >= len(simulated_actions):
                break
            action = simulated_actions[action_index]
            action_index += 1
        if action == 'y':
            playercard.append(deal_card(deck))
            print(f"Your Cards: {playercard} (Score: {calculatedscore(playercard)})")
        else:
            break
    return playercard
def dealer_turn(dealercard, deck):
    while calculatedscore(dealercard) < 17:
        dealercard.append(deal_card(deck))
    return dealercard
def play_blackjack(interactive=True, simulated_actions=None):
    global card_deck
    if not interactive and simulated_actions is None:
        simulated_actions = ['y', 'n']
    playercard = [deal_card(card_deck), deal_card(card_deck)]
    dealercard = [deal_card(card_deck), deal_card(card_deck)]
    print(f"Your Cards: {playercard} (Score: {calculatedscore(playercard)})")
    print(f"Dealer's visible card: {dealercard[0]}")
    playercard = player_turn(playercard, card_deck, interactive, simulated_actions)
    if calculatedscore(playercard) > 21:
        print(f"Your Cards: {playercard} (Score: {calculatedscore(playercard)})")
        print("Busted! Dealer wins.")
        return
    dealercard = dealer_turn(dealercard, card_deck)
    print(f"Your Cards: {playercard} (Score: {calculatedscore(playercard)})")
    print(f"Dealer's Cards: {dealercard} (Score: {calculatedscore(dealercard)})")
    player_score = calculatedscore(playercard)
    dealer_score = calculatedscore(dealercard)
    if dealer_score > 21 or player_score > dealer_score:
        print("Congrats! You win!")
    elif player_score < dealer_score:
        print("Better Luck Next Time!")
    else:
        print("So Close, It's a Tie!")
play_blackjack(interactive=True)
