
#   '''''''''''''''''''''''''''''''''''' THE HANGMAN GAME ''''''''''''''''''''''''''''''''

#Importig libraries

import random
import turtle

#Words for the game

def word_list():

    words = ['python','chrome','program' ,'science','algorithm','computing']
    return random.choice(words)

#For displaying the guessed letters in the game
 
def display(word,guessed):
    return ' '.join([letter if letter in guessed else '_' for letter in word])

#Graphics

#For Hanging man

def depicting_hangman():
    sc = turtle.Screen()
    sc.bgcolor("lightcoral")

    hangman = turtle.Turtle()
    hangman.speed(5)

    #for gallows

    #Base
    hangman.penup()
    hangman.goto(-100,-150)
    hangman.pendown()
    hangman.forward(200)

    #Vertical pole
    hangman.backward(100)
    hangman.left(90)
    hangman.forward(300)

    #Horizontal top bar
    hangman.right(90)
    hangman.forward(100)

    #rope
    hangman.right(90)
    hangman.forward(50)

    #hangman head
    hangman.penup()
    hangman.goto(50,50)
    hangman.pendown()
    hangman.circle(50)

    #Face
    
    # Draw the eyes
    eye_size = 10

    # Left eye
    hangman.penup()
    hangman.goto(75, 60)
    hangman.pendown()
    hangman.setheading(45)  # Angle for cross
    for _ in range(4):  # Draw cross
        hangman.forward(eye_size)
        hangman.backward(eye_size)
        hangman.right(90)

    # Right eye
    hangman.penup()
    hangman.goto(120, 60)
    hangman.pendown()
    hangman.setheading(45)  # Angle for cross
    for _ in range(4):  # Draw cross
        hangman.forward(eye_size)
        hangman.backward(eye_size)
        hangman.right(90)

    # Draw the mouth
    hangman.penup()
    hangman.goto(90, 20)
    hangman.setheading(0)  # Horizontal line
    hangman.pendown()
    hangman.forward(20)

    #body
    hangman.penup()
    hangman.goto(98,0)
    hangman.setheading(-90)  # Point downwards
    hangman.pendown()
    hangman.forward(100)

    # Draw the left arm
    hangman.penup()
    hangman.goto(98, -20)
    hangman.setheading(180)  # Point left
    hangman.pendown()
    hangman.forward(50)  # Left arm

    # Draw the right arm
    hangman.penup()
    hangman.goto(98, -20)
    hangman.setheading(0)  # Point right
    hangman.pendown()
    hangman.forward(50)  # Right arm

    # Draw the left leg
    hangman.penup()
    hangman.goto(98, -100)
    hangman.setheading(-135)  # Point downwards to the left
    hangman.pendown()
    hangman.forward(50)  # Left leg

    # Draw the right leg
    hangman.penup()
    hangman.goto(98, -100)
    hangman.setheading(-45)  # Point downwards to the right
    hangman.pendown()
    hangman.forward(50)  # Right leg


    hangman.hideturtle()
    turtle.done()


#For Survived Man

def draw_jumping_happy_man():
    sc = turtle.Screen()
    sc.bgcolor("lightblue")  # Background color

    man = turtle.Turtle()
    man.speed(3)

    # Draw the head
    man.penup()
    man.goto(0, 0)
    man.pendown()
    man.color("black")
    man.circle(50)  # Head

    # Draw the eyes
    man.penup()
    man.goto(-20, 60)
    man.pendown()
    man.color("black")
    man.dot(10)  # Left eye

    man.penup()
    man.goto(20, 60)
    man.pendown()
    man.dot(10)  # Right eye

    # Draw the mouth (happy)
    man.penup()
    man.goto(-20, 40)
    man.setheading(-60)  # Angle for a smiling mouth
    man.pendown()
    man.color("black")
    man.circle(20, 120)  # Smile

    # Draw the body
    man.penup()
    man.goto(0, 0)
    man.setheading(-90)  # Point downwards
    man.pendown()
    man.color("black")
    man.forward(100)  # Body

    # Draw the left arm (up)
    man.penup()
    man.goto(0, -40)
    man.setheading(155)  # Point diagonally up and left
    man.pendown()
    man.forward(75)  # Left arm

    # Draw the right arm (up)
    man.penup()
    man.goto(0, -40)
    man.setheading(25)  # Point diagonally up and right
    man.pendown()
    man.forward(75)  # Right arm

    # Draw the left leg (down)
    man.penup()
    man.goto(0, -100)
    man.setheading(-135)  # Point diagonally down and left
    man.pendown()
    man.forward(60)  # Left leg

    # Draw the right leg (down)
    man.penup()
    man.goto(0, -100)
    man.setheading(-45)  # Point diagonally down and right
    man.pendown()
    man.forward(60)  # Right leg

    man.hideturtle()
    turtle.done()


#Hangman game logic

def hang_man():
    word_to_guess = word_list()
    guessed = []
    attempts = 6
    word_guessed = False

    print("Welcome To Hangman !!! " )

    while attempts > 0 and not word_guessed:
        print("\n" + display(word_to_guess,guessed))
        print(f"Attempts remaining : {attempts}")

        guess = input("Guess a letter :").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("please guess a single letter.")
            continue

        if guess in guessed:
            print("You have already guessed that letter ")
            continue

        guessed.append(guess)

        if guess in word_to_guess:
            print(f'Good guess! {guess} is in the word')

        else:
            attempts-= 1
            print("Sorry ! wrong guess")

        if all(letter in guessed for letter in word_to_guess):
            word_guessed = True

        
    if word_guessed:
        print(f"Congratulations! you`ve guessed the word {word_to_guess} correctly !! \n You have saved the man from being hang !")
        draw_jumping_happy_man()

    else:
        print(f'Sorry you lose , the correct word was {word_guessed}... \n A man has been hanged because you lose..')

        depicting_hangman()

hang_man()       