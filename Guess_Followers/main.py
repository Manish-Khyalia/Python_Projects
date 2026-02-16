import random
from game_data import data
from art import logo, vs
def guess_followers() :
    print(logo)
    data1 = random.choice(data)
    data2 = random.choice(data)
    while data2 == data1 :
        data2 = random.choice(data)
    game_over = False
    current_score = 0
    while not game_over :

        if current_score > 0 :
            print(f"You're right! Current score: {current_score}.")
        print(f"Compare A: {data1['name']}, a {data1['description']}, from {data1['country']}.")
        print(vs)
        print(f"Against B: {data2['name']}, a {data2['description']}, from {data2['country']}.")
        compare = input("Who has more followers? Type 'A' or 'B': ").upper()
        if compare == "A" and data1['follower_count'] > data2['follower_count'] :
            current_score += 1
        elif compare == "B" and data2['follower_count'] > data1['follower_count'] :
            current_score += 1
        elif compare not in ["A", "B"] :
            print("Invalid input. Please type 'A' or 'B'.")
        else :
            print("\n"*20)
            print(logo)
            print(f"Sorry that's wrong. Final score: {current_score}")
            break

        data1 = data2
        data2 = random.choice(data)
        while data1 == data2 :
            data2 = random.choice(data)
        print("\n"*20)
def start() :

    over = False
    while not over :
        choice = input(
            "Do you want to play a game where you guess the number of instagram followers? Type 'y' or 'n': ").lower()
        if choice == "y" :
            guess_followers()
        else :
            over = True
start()
