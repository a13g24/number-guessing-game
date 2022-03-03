"""
Project 1 - Number Guessing Game
--------------------------------
"""

import random
from statistics import mean, median, multimode

record = []

def start_game():
    print("** Welcome to the guessing game! **")
    
    best_score = 0 if len(record) == 0 else min(record)
    
    print(f"Current best score: {best_score}\n")

    solution = random.randint(1, 100)
    
    num_guesses = 0
    
    while True:
        try:
            guess = input("Guess an integer between 1 and 100 inclusive: ")
            
            if not guess.isnumeric() or int(guess) < 1 or int(guess) > 100:
                raise ValueError("  ERROR: Your guess must be an INTEGER within the range of 1 to 100 inclusive.")
                
            guess = int(guess)

            num_guesses += 1
        except ValueError as ve:
            print(ve)
        else:
            if guess > solution:
                print("It's lower")
            elif guess < solution:
                print("It's higher")
            else:
                print(f"\nYou got it in {num_guesses} attempts!")
                record.append(num_guesses)
                break
            
    # print stats
    print(f"\nSTATISTICS\n Number of attempts: {len(record)}")
    print(f" Mean: {round(mean(record), 2)}\n Median: {median(record)}\n Mode(s): {multimode(record)}\n")


# Kick off the program by calling the start_game function.
ans = "y"
while ans == "y":
    start_game()
    
    ans = input("Would you like to play again (y/n)? ")[0].lower() 
    
    print()
    
    if ans == "n":
        print("                            Goodbye...")
    