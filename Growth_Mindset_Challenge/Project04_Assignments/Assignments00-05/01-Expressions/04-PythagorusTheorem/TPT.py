#Library
import math  

def calculate_hypotenuse():
    """Calculates the hypotenuse using the Pythagorean theorem."""
    try:
        # user interface
        ab = float(input("Enter the length of AB: "))
        ac = float(input("Enter the length of AC: "))

        # Applying Pythagorus calculation
        bc = math.sqrt(ab**2 + ac**2)

        overall = f"\033[1;3;4m{bc:.2f}\033[0m"

        # result
        print(f"\nThe length of BC (the hypotenuse) is: {overall}")

    except ValueError:
        print("Invalid input! Please enter numeric values.")

calculate_hypotenuse()
