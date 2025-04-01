def tall_enough():
    """Checking  if the user meets the minimum height requirement."""
    min_height = 50
    height = int(input("How tall are you? "))

    if height >= min_height:
        print("You're tall enough to ride!")
    else:
        print("You're not tall enough to ride, but maybe next year!")

def tall_enough_extension():
    """Continuously asks for height until the user enters nothing."""
    min_height = 50

    while True:
        height = input("How tall are you? (Press Enter to quit) ")

        if height == "":
            print("Exiting the program. Have a great day!")
            break
        
        height = int(height)

        if height >= min_height:
            print("You're tall enough to ride!")
        else:
            print("You're not tall enough to ride, but maybe next year!")


tall_enough_extension()
