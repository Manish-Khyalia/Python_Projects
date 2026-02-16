import random
from art import logo
print(logo)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def your_cards() :
    return random.choice(cards)

def dealer_cards() :
    return random.choice(cards)
def blackjack() :
    your_cards_list = []
    dealer_cards_list = []
    for card in range(2) :
        your_cards_list.append(your_cards())
    print(f"your cards: {your_cards_list}, current score {sum(your_cards_list)} ")
    for card in range(2) :
        dealer_cards_list.append(dealer_cards())
    print(f"Computer's first card: {dealer_cards_list[0]}")
    game_over = False
    while not game_over :


        choice = input("Type 'y' to get another card, type 'n' to pass : ").lower()

        if choice == "y" :
            your_cards_list.append(your_cards())
            if 11 in your_cards_list and sum(your_cards_list) > 21 :
                for key in range(len(your_cards_list)):
                    if your_cards_list[key] == 11:
                        your_cards_list[key] = 1

            print(f"Your cards: {your_cards_list}, current score {sum(your_cards_list)}")
            print(f"Computer's first card: {dealer_cards_list[0]}")
            if sum(your_cards_list) >21 :
                print(f"Your final hand: {your_cards_list}, final score {sum(your_cards_list)} ")
                print(f"Computer final hand: {dealer_cards_list}, final score {sum(dealer_cards_list)}")
                print("You went over. You lose 🙃")
                game_over = True


        elif choice == "n" :
            while sum(dealer_cards_list) < 17:
                dealer_cards_list.append(dealer_cards())
                if 11 in dealer_cards_list and sum(dealer_cards_list) > 21:
                    for key in range(len(dealer_cards_list)):
                        if dealer_cards_list[key] == 11:
                            dealer_cards_list[key] = 1
            print(f"Your final hand: {your_cards_list}, final score {sum(your_cards_list)} ")
            print(f"Computer final hand: {dealer_cards_list}, final score {sum(dealer_cards_list)}")
            if sum(dealer_cards_list) > 21:
                print(f"Your final hand: {your_cards_list}, final score {sum(your_cards_list)} ")
                print(f"Computer final hand: {dealer_cards_list}, final score {sum(dealer_cards_list)}")
                print("Computer went over. You win 😃")
                game_over = True
            else :

                if sum(your_cards_list) > sum(dealer_cards_list) :
                    print("You win 😃")
                elif sum(your_cards_list) < sum(dealer_cards_list) :
                    print("Computer win 😤")
                else :
                    print("It's a draw 🙃")
                game_over = True

def play_game():
    while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == 'y' :
        print("\n"*20)
        blackjack()
play_game()


