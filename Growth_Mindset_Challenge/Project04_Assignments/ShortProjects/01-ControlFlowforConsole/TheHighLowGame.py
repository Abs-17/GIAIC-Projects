
'''-----------------------------------The High Low Game -------------------------------------------'''

#Library
import random

def high_low_game(rounds=5):
    """Plays the High-Low game for a given number of rounds."""
    score = 0  

    print("🎲 Welcome to the High-Low Game!")
    print(f"You will play {rounds} rounds.\n")

    for round_num in range(1, rounds + 1):
        user_number = random.randint(1, 100)
        computer_number = random.randint(1, 100)

        print(f"🔢 Round {round_num}: Your number is {user_number}")
        guess = input("Do you think your number is (H)igher or (L)ower than the computer's? ").strip().lower()

        if (guess == "h" and user_number > computer_number) or (guess == "l" and user_number < computer_number):
            print("✅ Correct! You get a point.\n")
            score += 1
        else:
            print(f"❌ Wrong! The computer's number was {computer_number}.\n")

    print(f"🎯 Game Over! Your final score: {score}/{rounds}")


high_low_game()
