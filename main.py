from random import randint

logo = """
  _   _                       _                   _____                     
 | \ | |                     | |                 / ____|                    
 |  \| | ___  _   _ _ __ ___ | |__   ___ _ __   | |  __ _   _  ___  ___ ___
 | . ` |/ _ \| | | | '__/ _ \| '_ \ / _ \ '__|  | | |_ | | | |/ _ \/ __/ __|
 | |\  |  __/| |_| | | | (_) | |_) |  __/ |     | |__| | |_| |  __/\__ \__ \
 |_| \_|\___| \__,_|_|  \___/|_.__/ \___|_|      \_____|\__,_|\___||___/___/
                            NUMBER GUESSER
"""

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(guess, answer, turns):
    """checks answer against guess. Returns the number of turns remaining."""
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")

def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    answer = randint(1, 100)
    turns = set_difficulty()

    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining.")
        try:
            guess = int(input("Make a guess: "))
        except:
            print("Please enter a valid number.")
            continue

        turns = check_answer(guess, answer, turns)

        if turns == 0:
            print("You've run out of guesses. You lose!")
            print(f"The answer was {answer}.")
            return
        elif guess != answer:
            print("Guess again.\n")

game()
