#Library
import random

Rolls = 3

def Dice_Simulator():
    print("The Dice Rolling Simulator")
    '''Making simulation for putting the Dice on roll..'''
    for i in range(1,Rolls + 1):
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        print(f"Roll the Dice : Dice 01 is {dice1} , Dice 02 is {dice2}")

if __name__=='__main__':
    Dice_Simulator()
    