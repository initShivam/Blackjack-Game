print("Welcome to the BlackJack Game!")
print('''
╭────────────╮  ╭────────────╮  ╭────────────╮
│ K          │  │ Q          │  │ A          │
│            │  │            │  │            │
│     ♥      │  │     ♥      │  │     ♥      │
│            │  │            │  │            │
│          K │  │          Q │  │          A │
╰────────────╯  ╰────────────╯  ╰────────────╯
''')
print(" ")
print("The rules are simple:")
print("1. You will be dealt two cards.")
print("2. You can choose to 'hit' (get another card) or 'stand' (keep your current hand).")
print("3. The goal is to get as close to 21 as possible without going over.")
print("4. If you go over 21, you lose.")
print("5. If you get 21, you win!")
print("6. The dealer will also play, and you want to beat the dealer's hand.")
print("7. Aces can be worth 1 or 11, face cards are worth 10, and all other cards are worth their number.")
print(" ")
print("Let's start the game!")
print(" ")
print("Type 'exit' to quit the game at any time.")                  

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
import random

player_hand = []
dealer_hand = []
def deal_card():
    """Returns a random card from the deck."""
    return random.choice(cards)

print("Dealing cards...")
print(" ")

for _ in range(2):
    player_hand.append(deal_card())
    dealer_hand.append(deal_card())
    print(f"Your hand: {player_hand}, current score: {sum(player_hand)}")
    # print(f"Dealer's hand: {dealer_hand[0]}, current score: {sum(dealer_hand)}")
    print(f"Dealer's hand: {dealer_hand[0]}, current score: Hidden")
    print("")

# print("Your current hand:", player_hand, "Score:", sum(player_hand))
# print("Dealer's current hand:", dealer_hand[0], "and a hidden card.")
print("")
print("Type 'hit' to get another card or 'stand' to keep your current hand.")

while True:
    action = input("What would you like to do? (hit/stand): ").lower()

    if action == "hit":
        player_hand.append(deal_card())
        print("Your hand:", player_hand, "Score:", sum(player_hand))
        if sum(player_hand) > 21:
            print("You went over 21! You lose.")
            print(f"Dealer's hand: {dealer_hand}, current score: {sum(dealer_hand)}")
            break
    elif action == "stand":
        print("You chose to stand.")
        break
    elif action == "exit":
        print("Thanks for playing!")
        exit()
    else:
        print("Invalid input. Please type 'hit' or 'stand'.")

if sum(player_hand) == 21:
    print("Blackjack! You win!")
    print(f"Dealer's hand: {dealer_hand}, current score: {sum(dealer_hand)}")
elif sum(player_hand) < 21:
    print("Dealer's turn...")
    while sum(dealer_hand) < 17:
        dealer_hand.append(deal_card())
        print("Dealer's hand:", dealer_hand, "Score:", sum(dealer_hand))

    if sum(dealer_hand) > 21:
        print("Dealer went over 21! You win!")
    elif sum(dealer_hand) == sum(player_hand):
        print("It's a draw!")
    elif sum(dealer_hand) > sum(player_hand):
        print("Dealer wins!")
    else:
        print("You win!")
    print(f"Dealer's hand: {dealer_hand}, current score: {sum(dealer_hand)}")