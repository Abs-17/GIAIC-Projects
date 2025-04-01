def guess_():
    print("\5 Lets Play a Game !!!! \n Think of a number between 1 and 100 , And Im the one who will guess it....")

    low = 1
    high = 100
    tries = 0

    s = input("Press Enter to continue...")
    print(s)
 

    while True:
        guess = (low + high) // 2
        tries += 1

        print(f"My guess is {guess}. ")

        response = input("is it (h)igh , (l)ow or (c)orrect ?").lower()

        if response == 'c':
            print(f"Yay !! I guessed the number in just {tries} tries.")
            break
        elif response == 'h':
            high = guess - 1
        elif response == 'l':
            low = guess +1
        else:
            print("please enter 'h' , 'l' or 'c' .")


guess_()




