import random

# Making an intro to Game
def guess():
    print("Welcome to GUESS THE NUMBER GAME !!!")
    _p = input("Press Enter to explain the details of the game .....")
    print(_p)
    p_ = input("The computer randomly selects a number between 1 and 100.\n"
               "The player is prompted to guess the number.\n"
               "The game gives feedback if the guess is too high or too low.\n"
               "The game keeps track of how many attempts the player takes to guess correctly....\n"
               "Press Enter to start.....")
    print(p_)
    print("I'm thinking of a number between 1 and 100.")

    # Building the logic behind the game
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed = False

    # Loop until the user guesses the number
    while not guessed:
        try:
            # Player's guess
            player_guess = int(input("Take a guess: "))
            attempts += 1

            # Check if the guess is too high, too low, or correct
            if player_guess < number_to_guess:
                print("Your guess is too low.")
            elif player_guess > number_to_guess:
                print("Your guess is too high.")
            else:
                guessed = True
                print(f"Congratulations! You've guessed the correct number {number_to_guess} in {attempts} attempts.")

        # Adding exception handling for non-integer input
        except ValueError:
            print("Please enter a valid number.")

# Call the guess function to start the game
guess()