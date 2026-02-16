from art import logo
import random
easy_level_turns = 10
hard_level_turns = 5

def guess_number() :
    print(logo)
    random_number = random.randint(1, 100)
    print("Welcome to the number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    turn = 0
    difficulty = input("Choose difficulty level. Type 'easy' or 'hard': ").lower()
    if difficulty == "easy" :
        turn = easy_level_turns
    elif difficulty == "hard" :
        turn = hard_level_turns
    else :
        print("Please choose only 'easy' or 'hard'.")
        return
    for i in range(turn) :
        print(f"You have {turn - i} attempts remaining to guess the number. ")
        guess = int(input("Make a guess: "))
        if random_number == guess :
            print(f"You got it! The answer was {guess}.")
            break
        elif abs(guess - random_number) <= 2 :
            print("Too close.")
        elif guess < random_number :
            print("Too low.")
        else :
            print("Too high.")
    else :
        print(f"You lose. The correct number is {random_number}")


def guess_again() :
    over = False
    while not over :
        choice = input("Do you want to play the guessing game? Type 'y' or 'n': ")
        if choice == "y" :
            guess_number()
            print("/n"*20)
        else :
            over = True
guess_again()



