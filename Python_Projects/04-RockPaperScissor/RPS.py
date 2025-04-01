import random

def rps():
    choices = ['rock', 'paper','scissor']

    rules = {
        'rock' : 'scissor',
        'paper' : 'rock',
        'scissor' : 'paper'
    }

#logic
    while True :
        print("\n rock , paper or scissor ? \n press 'x' to exit ")
        user_choice = input('your choice : ').lower()

        if user_choice == 'x':
            print('Thanks for playing , Good Bye !!')
            break
        
        if user_choice not in choices:
            print("Invalid choice")
            continue

        comp_choice = random.choice(choices)
        print(f"Computer chose: {comp_choice}")
        
        if user_choice == comp_choice:
            print("It's a tie!")
        elif rules[user_choice] == comp_choice:
            print("You win!")
        else:
            print("You lose!")

rps()            

